import re
import time
import pytest

from src.app.constants import Gender
from src.app.features.common import Common
from src.app.features.landing import Landing
from src.app.features.organizing import Organizing


class Login(Common):

    def __init__(self, **kwargs):
        super().__init__(page=__class__.__name__, **kwargs)

    def validate(self):
        self.find_element_by_accessibility_id('Welcome to').is_displayed()
        self.find_element_by_accessibility_id('Wildkard!').is_displayed()

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
            if 'confirmation code is' in res:
                return re.search(r'\d{5}', res).group()
            time.sleep(0.1)
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
        else:
            raise AssertionError('Unexpected state occurred')

    def fill_profile(self):
        self.send_keys(el=self.find_element_by_accessibility_id('rainbowdash'),
                       data="special_one")
        self.send_keys(el=self.find_element_by_accessibility_id('Cristiano Ronaldo'),
                       data="José Mourinho")
        self.find_element_by_accessibility_id('sighUpDatePicker').click()
        self.find_elements_by_xpath('//XCUIElementTypeOther')[0].click()
        self.find_element_by_accessibility_id('ios_touchable_wrapper').click()
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypePickerWheel'),
                       data=Gender.PreferNotToSay.value)
        self.find_element_by_accessibility_id('ios_modal_top').click()
        self.click__sign_up()

    def click__login_on_profile(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="Log In"])[4]').click()

    def select_sport__soccer(self):
        self.find_element_by_accessibility_id('Soccer').click()

    def select_sport__basketball(self):
        self.find_element_by_accessibility_id('Basketball').click()

    def type_league_name(self):
        self.send_keys(el=self.find_element_by_accessibility_id('League Name'),
                       data="Super League")

    def click__create_league(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="Create League"])[4]').click()

    def create_league_soccer(self):
        self.select_sport__soccer()
        self.type_league_name()
        self.click__create_league()

    @staticmethod
    def go_to_landing():
        return Landing()

    @staticmethod
    def go_to_organizing():
        return Organizing()
