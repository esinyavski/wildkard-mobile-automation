from src.app.features.common import Common


class Landing(Common):

    def __init__(self, **kwargs):
        super().__init__(page=__class__.__name__, **kwargs)

    def validate(self):
        self.find_element_by_xpath('//XCUIElementTypeStaticText[@name="CHANNELS"]').is_displayed()

    def click__yes_this_is_correct(self):
        self.tap(self.find_element_by_accessibility_id('Yes, this is correct'))

    def click__log_out(self):
        self.tap(self.find_element_by_accessibility_id('Log out'))

