"""
A wrapper around Appium library to make UI actions
"""

from appium import webdriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.utils.logger import Logger
from src.utils.config_parser import Config


class Driver:
    logger = Logger.get_logger(__name__)
    driver: WebDriver = None
    config: Config = None
    wait: WebDriverWait
    action: TouchAction = None
    keys = Keys

    @classmethod
    def init_driver(cls, config: Config):
        cls.config = config

        desired_caps = {'platformName': config.platformName,
                        'platformVersion': config.platformVersion,
                        'deviceName': config.deviceName,
                        'udid': config.udid,
                        "xcodeOrgId": config.xcodeOrgId,
                        "xcodeSigningId": config.xcodeSigningId,
                        "bundleId": config.bundleId,
                        "noReset": True}

        driver = webdriver.Remote(config.appiumUrl, desired_caps)
        driver.implicitly_wait(config.waiting_time)
        cls.driver = driver
        cls.wait = WebDriverWait(driver, config.waiting_time)
        cls.action = TouchAction(driver)

    def __init__(self, **kwargs):
        assert self.driver

    def find_element_by_accessibility_id(self, locator):
        return self.driver.find_element_by_accessibility_id(locator)

    def find_elements_by_accessibility_id(self, locator):
        return self.driver.find_elements_by_accessibility_id(locator)

    def find_element_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def find_elements_by_xpath(self, locator):
        return self.driver.find_elements_by_xpath(locator)

    def tap(self, el: WebElement):
        self.action.tap(el).perform()

    @staticmethod
    def clear(el: WebElement):
        el.click()
        el.clear()

    @staticmethod
    def send_keys(el: WebElement, data: str):
        el.click()
        el.send_keys(data)

    def wait_until_visible(self, locator):
        by = By.XPATH if "/" in locator else By.ID
        return self.wait.until(ec.visibility_of_element_located((by, locator)))
