from src.utils import constants
from src.utils.common_actions import Utilities

_hotel = '//nav//a[@href="https://www.makemytrip.com/hotels/"]'
_li_login = "//li[contains(.,'Login or Create')]"
_input_login_popup_username = "//input[@id='username']"
_button_continue = "//button[@data-cy='continueBtn']"
_input_login_popup_password = "//input[@data-cy='password']"
_button_login = "//button[@data-cy='login']"
_icon_close_popup = "//span[contains(@data-cy,'modalClose')]"


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utilities(self.driver)
        self.clicks = self.utils.click_activity
        self.inputs = self.utils.enter_text_

    def select_hotel(self):
        self.login()
        self.clicks(element=_hotel, locator_type='xpath')

    def login(self):
        self.clicks(element=_li_login)
        self.inputs(element=_input_login_popup_username, text=constants.USER)
        self.clicks(element=_button_continue)
        self.inputs(element=_input_login_popup_password, text=constants.PWD)
        self.clicks(element=_button_login)
        self.clicks(element=_icon_close_popup)