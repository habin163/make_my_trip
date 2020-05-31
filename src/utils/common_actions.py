"""
Consists of common actions utilized across the App
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from src.utils import constants


class Utilities:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.locator = {
            'name': self.driver.find_element_by_class_name,
            'xpath': self.driver.find_element_by_xpath,
            'css': self.driver.find_element_by_css_selector
        }
        default = self.driver.find_element_by_xpath
        self.actions = ActionChains(self.driver)

    def click_activity(self, element: str, locator_type: str = 'xpath'):
        # TODO Add wait element before clicking, dynamic wait
        self.driver.implicitly_wait(constants.MAX_WAIT_TIME)
        _click_element = self.locator.get(locator_type.lower(), None)(element)
        # self.bring_element_in_viewport(element=_click_element)
        _click_element.click()

    def enter_text_(self, element: str, locator_type: str = 'xpath', text="hello"):
        # TODO Add wait element before clicking, dynamic wait
        self.click_activity(element=element, locator_type=locator_type)
        input_element = self.locator.get(locator_type.lower(), None)(element)
        input_element.clear()
        input_element.send_keys(text)

    def slider_action(self, element: str, locator_type: str = 'xpath', h_value=0, v_value=0):
        # TODO Add wait element before clicking, dynamic wait
        slider_element = self.locator.get(locator_type.lower(), None)(element)
        self.bring_element_in_viewport(element=slider_element)
        self.actions.drag_and_drop_by_offset(source=slider_element, xoffset=h_value, yoffset=v_value).perform()

    def bring_element_in_viewport(self, element: WebElement):
        if isinstance(element,str):
            element = self.locator.get('xpath')(element)
        skip_height = int(self.get_elem_attr(element="//div[@id='listingView']", attr_type='offsetHeight'))
        self.driver.execute_script(f"arguments[0].scrollIntoView();window.scrollBy(0,{-1.5*skip_height})", element)
        time.sleep(constants.SCROLL_VIEWPORT_WAIT)
        self.actions.move_to_element(element)
        time.sleep(constants.SCROLL_VIEWPORT_WAIT - 1)

    def element_enabled(self, element: str, locator_type: str = 'xpath'):
        element = self.locator.get(locator_type.lower())(element)
        return element.is_enabled()

    def element_displayed(self, element: str, locator_type: str = 'xpath'):
        element = self.locator.get(locator_type.lower())(element)
        return element.is_displayed()

    def element_selected(self, element: str, locator_type: str = 'xpath'):
        element = self.locator.get(locator_type.lower())(element)
        return element.is_selected()

    def clear_overlay(self, element: str, locator_type: str = 'xpath'):
        if self.element_displayed(element=element, locator_type=locator_type):
            self.click_activity(element=element, locator_type=locator_type)

    def get_elem_attr(self, element: str, locator_type: str = 'xpath', attr_type='innerText') -> str:
        element = self.locator.get(locator_type.lower(), None)(element)
        return element.get_attribute(attr_type)
