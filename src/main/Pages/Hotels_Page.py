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


class HotelsPage:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utilities(driver=self.driver)

    def add_rooms(self, rooms=2, adutls_per_room=2, childeren_per_room=2):
        self.utils.click_activity(element=_guest_label)
        for room in range(rooms):
            self.utils.click_activity(element=_adult_count.format(adutls_per_room))
            self.utils.click_activity(element=_childer_count.format(childeren_per_room))
            if rooms > 1:
                self.utils.click_activity(element=_add_another_room_button)
        self.utils.click_activity(element=_button_submit_room)

    def add_travelling_for(self, travelling_for="Work"):
        self.utils.click_activity(element=_label_travel_for)
        self.utils.click_activity(element=_li_travel_for.format(travelling_for.title()))

    def search_itenary(self):
        self.utils.click_activity(element=_button_submit_search)
