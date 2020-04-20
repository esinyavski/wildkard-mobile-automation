import time
import pytest

from src.app.features.common import Common
from src.app.features.organizing import Organizing


class Landing(Common):

    def __init__(self, **kwargs):
        super().__init__(page=__class__.__name__, **kwargs)

    def validate(self):
        if self.check_landing_page():
            return
        elif self.check_welcome_page():
            pytest.skip("You are on the Welcome page. Run login test before.")
        else:
            raise AssertionError("landing page is not displayed")

    def go_to_dashboard(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="DASHBOARD, tab, 1 of 5"]').click()

    def go_to_search(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="SEARCH, tab, 2 of 5"]').click()

    def go_to_important(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="IMPORTANT, tab, 3 of 5"]').click()

    def go_to_dialog(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="DIALOG, tab, 4 of 5"]').click()

    def go_to_notification(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="NOTIFICATION, tab, 5 of 5"]').click()

    def click__league_menu(self):
        # temporary implementation due to unreachable UI element
        time.sleep(4)
        self.action.tap(x=278, y=57).perform()

    def click__create_new_league(self):
        self.find_elements_by_xpath('//XCUIElementTypeOther[@name="Create new League"]')[-1].click()

    def select_sport__soccer(self):
        self.find_element_by_accessibility_id('Soccer').click()

    def select_sport__basketball(self):
        self.find_element_by_accessibility_id('Basketball').click()

    def type_league_name(self, name):
        self.send_keys(el=self.find_element_by_accessibility_id('League Name'),
                       data=name)

    def click__create_league(self) -> Organizing:
        self.find_elements_by_xpath('//XCUIElementTypeOther[@name="Create League"]')[-1].click()
        time.sleep(1)
        if "Organization already exist" in self.driver.page_source:
            pytest.skip("Organization already exists. Please clean app's DB before test run")
        return Organizing()

    def select_league_from_menu(self, name) -> Organizing:
        self.find_elements_by_xpath(f'//XCUIElementTypeOther[@name="{name} ORGANIZER"]')[0].click()
        return Organizing()

    def select_league_from_page(self, name):
        els = self.find_elements_by_xpath(f'//XCUIElementTypeOther[starts-with(@name, "{name}")]')
        if not els:
            raise AssertionError(f"There is no league `{name}` on the landing page")
        else:
            els[0].click()

    def accept_invitation(self):
        self.find_elements_by_xpath('//XCUIElementTypeOther[@name="Yes"]')[-1].click()

    def check_team_displayed(self, name):
        self.find_element_by_xpath(f'//XCUIElementTypeOther[@name="{name}"]').is_displayed()

    def select_team_from_page(self, name):
        els = self.find_elements_by_xpath(f'//XCUIElementTypeOther[starts-with(@name, "{name}")]')
        if not els:
            raise AssertionError(f"There is no team `{name}` on the landing page")
        else:
            els[0].click()

    def send_message_to_chat(self):
        # write
        msg = self.dummy.gen_string()
        self.send_keys(el=self.find_element_by_xpath('//*[@name="Write a message"]/XCUIElementTypeTextField'),
                       data=msg)
        # send
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="GIF"])[2]/XCUIElementTypeOther[2]').click()
        # check
        self.find_element_by_xpath(f'//XCUIElementTypeStaticText[@name="{msg}"]').is_displayed()

    def send_gif_to_chat(self):
        # click on the gif option
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="GIF"])[2]').click()
        # select the first suggested gif
        self.find_element_by_xpath(
            '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther').click()
        # check
        assert len(self.find_elements_by_xpath('//XCUIElementTypeOther[2]/XCUIElementTypeImage')) > 1

