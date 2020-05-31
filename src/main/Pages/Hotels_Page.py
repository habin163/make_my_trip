from src.main.Pages.Navigation_Page import NavigationPage
from src.utils.common_actions import Utilities

_select_city_div = "//label[@for='city']/parent::div"
_input_city = "//input[@id='city']"
_guest_label = "//label[@for='guest']"
_childer_count = "//div[@class='roomsGuests']//li[@data-cy='children-{}']"
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
        self.clicks(element=_guest_label)
        for room in range(rooms):
            if room > 0:
                self.clicks(element=_add_another_room_button)
            self.clicks(element=_adult_count.format(adutls_per_room))
            self.clicks(element=_childer_count.format(childeren_per_room))

        self.clicks(element=_button_submit_room)

    def add_travelling_for(self, travelling_for="Work"):
        self.clicks(element=_label_travel_for)
        self.clicks(element=_li_travel_for.format(travelling_for.title()))

    def search_itenary(self):
        self.clicks(element=_button_submit_search)
