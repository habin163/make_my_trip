"""
Consists of common actions utilized across the App
"""
from selenium.webdriver.chrome.webdriver import WebDriver

from src.utils import constants


class Utilities:
    def __init__(self, driver):
        self.driver = driver
        self.locator = {
            'name': self.driver.find_element_by_class_name,
            'xpath': self.driver.find_element_by_xpath,
            'css': self.driver.find_element_by_css_selector
        }

    def click_activity(self, element: str, locator_type: str = 'xpath'):
        # TODO Add wait element before clicking, dynamic wait
        self.driver.implicitly_wait(constants.MAX_WAIT_TIME)
        self.locator.get(locator_type.lower(), None)(element).click()

    def enter_text_(self, element: str, locator_type: str = 'xpath', text="hello"):
        # TODO Add wait element before clicking, dynamic wait
        self.click_activity(element=element, locator_type=locator_type)
        input_element = self.locator.get(locator_type.lower(), None)(element)
        input_element.clear()
        input_element.send_keys(text)




