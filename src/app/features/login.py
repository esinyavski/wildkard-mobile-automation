import re
import time
import pytest

from src.app.constants import Gender
from src.app.features.common import Common
from src.app.features.landing import Landing


class Login(Common):

    def __init__(self, **kwargs):
        super().__init__(page=__class__.__name__, **kwargs)

    def validate(self):
        if self.check_welcome_page():
            return
        elif self.check_landing_page():
            self.logout()
        else:
            raise AssertionError("Welcome page is not displayed")

    def click__log_in(self):
        self.find_element_by_accessibility_id('Log In').click()

    def click__sign_up(self):
        self.find_element_by_accessibility_id('Sign Up').click()

    def click__continue(self):
        self.find_element_by_accessibility_id('Continue').click()

    def capture_code(self) -> str:
        start_time = time.time()

        while (time.time() - start_time) < self.config.waiting_time:
            res = self.driver.page_source
            if 'confirmation code' in res:
                return re.search(r'\d{5}', res).group()
        else:
            raise AssertionError(f"OTP is not received after waiting {self.config.waiting_time} sec.")

    def enter_code(self, code):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeTextField'),
                       data=code)

    def authenticate(self, phone_number, country):
        if country == 'belarus' and not self.find_elements_by_accessibility_id('🇧🇾 '):
            self.select_country_belarus()
        self.type_phone_number(phone_number)
        self.click__continue()
        if self.find_elements_by_accessibility_id('Enter the code'):
            code = self.capture_code()
            self.enter_code(code=code)
            self.click__continue()
        elif self.find_elements_by_accessibility_id('Your phone number already exists. Would you like to login?'):
            pytest.skip('Your phone number already exists.')
        elif self.find_elements_by_accessibility_id('We can’t find your number. Did you input it correctly?'):
            pytest.skip('We can’t find your number. Please sign up by this user before test run.')
        else:
            raise AssertionError('Unexpected state occurred')

    def fill_profile(self):
        self.find_element_by_accessibility_id('sighUpDatePicker').click()
        self.find_elements_by_xpath('//XCUIElementTypeOther')[0].click()
        self.find_element_by_accessibility_id('ios_touchable_wrapper').click()
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypePickerWheel'),
                       data=Gender.PreferNotToSay.value)
        self.find_element_by_accessibility_id('ios_modal_top').click()

    def click__sign_up_on_profile(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="Sign Up"])[4]').click()
        return Landing()

    def click__login_on_profile(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="Log In"])[4]').click()
        return Landing()

    def login(self):
        self.click__log_in()
        self.authenticate(
            phone_number=self.config.main_phone.number,
            country=self.config.main_phone.country)
        self.fill_profile()
        self.click__login_on_profile()

    def click__yes_this_is_correct(self):
        self.find_element_by_accessibility_id('Yes, this is correct').click()

    def click__log_out(self):
        self.find_element_by_accessibility_id('Log out').click()

    def click__user_menu(self):
        self.find_element_by_accessibility_id('userHeaderIconTouch').click()

    def logout(self):
        self.click__user_menu()
        self.click__log_out()
        return Login()

