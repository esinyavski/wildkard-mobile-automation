from src.app.interface import Interface


class Common(Interface):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self):
        pass

    def select_country_belarus(self):
        self.find_element_by_accessibility_id('🇺🇸 ').click()
        self.find_element_by_xpath('//*[@name="🇧🇾 Belarus (+375)"]').click()

    def select_country_usa(self):
        self.find_element_by_accessibility_id('🇧🇾 ').click()
        self.find_element_by_xpath('//*[@name="🇺🇸 United States (+1)"]').click()

    def type_phone_number(self, number: str):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeTextField'),
                       data=number)


