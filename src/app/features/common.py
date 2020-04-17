import time

from src.app.interface import Interface


class Common(Interface):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self):
        pass

    def check_landing_page(self):
        return len(self.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="CHANNELS"]')) > 0

    def check_welcome_page(self):
        return len(self.find_elements_by_accessibility_id('Welcome to')) > 0

    def check_notification(self, message):
        start_time = time.time()

        while (time.time() - start_time) < self.config.waiting_time:
            res = self.driver.page_source
            if message in res:
                return
            time.sleep(0.1)
        else:
            raise AssertionError(
                f"Notification is not received after waiting {self.config.waiting_time} sec.")

    def select_country_belarus(self):
        self.find_element_by_accessibility_id('🇺🇸 ').click()
        self.find_element_by_xpath('//*[@name="🇧🇾 Belarus (+375)"]').click()

    def select_country_usa(self):
        self.find_element_by_accessibility_id('🇧🇾 ').click()
        self.find_element_by_xpath('//*[@name="🇺🇸 United States (+1)"]').click()

    def type_phone_number(self, number: str):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeTextField'),
                       data=number)

