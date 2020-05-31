"""
Consists of common actions utilized across the App
"""
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from src.utils import constants


class Utilities:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.locator = {
            'name': self.driver.find_element_by_class_name,
            'xpath': self.driver.find_element_by_xpath,
            'css': self.driver.find_element_by_css_selector
        }
        self.by_locator = {
            'name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR
        }
        self.actions = ActionChains(self.driver)

    def click_activity(self, element: str, locator_type: str = 'xpath'):
        _click_element = self.get_exp_wait_element(element=element, locator_type=locator_type)
        _click_element.click()

    def enter_text_(self, element: str, locator_type: str = 'xpath', text="hello"):
        self.click_activity(element=element, locator_type=locator_type)
        input_element = self.locator.get(locator_type.lower(), None)(element)
        input_element.clear()
        input_element.send_keys(text)

    def slider_action(self, element: str, locator_type: str = 'xpath', h_value=0, v_value=0):
        slider_element = self.get_exp_wait_element(element=element, locator_type=locator_type)
        self.bring_element_in_viewport(element=slider_element)
        self.actions.drag_and_drop_by_offset(source=slider_element, xoffset=h_value, yoffset=v_value).perform()

    def bring_element_in_viewport(self, element: WebElement):
        if isinstance(element, str):
            element = self.get_exp_wait_element(element=element)
        skip_height = int(self.get_elem_attr(element="//div[@class='headerOuter']", attr_type='offsetHeight')) + 50
        self.driver.execute_script(f"arguments[0].scrollIntoView();window.scrollBy(0,{-skip_height})", element)
        self.wait_()

    def element_enabled(self, element: str, locator_type: str = 'xpath'):
        element = self.get_exp_wait_element(element=element, locator_type=locator_type)
        return element.is_enabled()

    def element_displayed(self, element: str, locator_type: str = 'xpath'):
        element = self.get_exp_wait_element(element=element, locator_type=locator_type)
        return element.is_displayed()

    def element_selected(self, element: str, locator_type: str = 'xpath'):
        element = self.get_exp_wait_element(element=element, locator_type=locator_type)
        return element.is_selected()

    def clear_overlay(self, element: str, locator_type: str = 'xpath'):
        if self.element_displayed(element=element, locator_type=locator_type):
            self.click_activity(element=element, locator_type=locator_type)

    def get_elem_attr(self, element: str, locator_type: str = 'xpath', attr_type='innerText') -> str:
        element = self.get_exp_wait_element(element=element, locator_type=locator_type)
        return element.get_attribute(attr_type)

    def wait_(self, max_wait=constants.SCROLL_VIEWPORT_WAIT):
        self.driver.implicitly_wait(max_wait)

    def get_exp_wait_element(self, element: str, locator_type: str = 'xpath'):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException,)
        return WebDriverWait(self.driver, constants.MAX_WAIT_TIME, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((self.by_locator.get(locator_type.lower(), None), element)))

    def scroll_and_click(self, element: str, locator_type: str = 'xpath'):
        element = self.get_exp_wait_element(element, locator_type)
        self.actions.click(on_element=element).perform()
