from src.main.Pages.Navigation_Page import NavigationPage
from src.utils import constants
from src.utils.common_actions import Utilities

_select_city_div = "//label[@for='city']/parent::div"
_input_city = "//input[@id='city']"
_input_dropdown_city = "//input[contains(@placeholder,'Hotel')]"
_li_first_option = "//li[@id='react-autowhatever-1-section-0-item-0']"
_input_dates = "//label[contains(@for,'checkin')]"
_div_date_picker = "//div[contains(@aria-label,'{}')]"
_guest_label = "//label[@for='guest']"

_children_count = "//div[@class='roomsGuests']//li[@data-cy='children-{}']"
_adult_count = "//div[@class='roomsGuests']//li[@data-cy='adults-{}']"
_add_another_room_button = "//button[@class='btnAddRoom']"
_button_submit_room = "//button[@data-cy='submitGuest']"
_label_travel_for = "//label[@for='travelFor']"
_li_travel_for = "//ul[@class='travelForPopup']/li[contains(.,'{}')]"
_button_submit_search = "//button[@id='hsw_search_button']"


class HotelsPage(NavigationPage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_rooms(self, rooms=2, adutls_per_room=2, childeren_per_room=2):
        self.clicks(element=_input_city)
        self.inputs(element=_input_dropdown_city, text=constants.LOCATION)
        self.utils.wait_(constants.MAX_WAIT_TIME)
        self.scroll_click(element=_li_first_option)
        self.utils.wait_(2.5*constants.MAX_WAIT_TIME)
        self.clicks(element=_div_date_picker.format(constants.IN_DAY))
        self.clicks(element=_div_date_picker.format(constants.OUT_DAY))
        self.clicks(element=_guest_label)
        for room in range(rooms):
            if room > 0:
                self.clicks(element=_add_another_room_button)
            self.clicks(element=_adult_count.format(adutls_per_room))
            self.clicks(element=_children_count.format(childeren_per_room))
        self.clicks(element=_button_submit_room)

    def add_travelling_for(self, travelling_for="Work"):
        self.clicks(element=_label_travel_for)
        self.clicks(element=_li_travel_for.format(travelling_for.title()))

    def search_itenary(self):
        self.clicks(element=_button_submit_search)
