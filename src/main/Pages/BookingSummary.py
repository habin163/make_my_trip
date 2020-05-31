"""
This consists of all details from editable Booking summary Page
"""
from src.main.Pages.Navigation_Page import NavigationPage

_summary_description_ = "//div[@class='summary_description']"
_sum_hotel_name = "//p[contains(@class,'hotel_name')]"
_sum_hotel_loc = "//p[contains(@class,'hotel_location')]"
_sum_check_in = "//p[contains(.,'CHECK IN')]/parent::div/p[@class='checkin_time']"
_sum_check_out = "//p[contains(.,'CHECK OUT')]/parent::div/p[@class='checkin_time']"
_sum_room_heading = "//span[contains(@class,'room_heading')]/span"
_sum_room_count = _summary_description_+"//p[@class='clearfix']/span"  #elements
_sum_traveller_name = _summary_description_+"//p[contains(@class,'traveler_name')]"
_sum_contact_info = "//p[contains(@class,'contact_info')]"


class BookingSummary(NavigationPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.get_attr = self.utils.get_elem_attr

    def fetch_summary_values(self):
        summary_info = dict()
        summary_info['hotel_name'] = self.get_attr(element=_sum_hotel_name)
        summary_info['hotel_location'] = self.get_attr(element=_sum_hotel_loc)
        summary_info['check_in'] = self.get_attr(element=_sum_check_in)
        summary_info['check_out'] = self.get_attr(element=_sum_check_out)
        summary_info['room_heading'] = self.get_attr(element=_sum_room_heading)
        summary_info['room_count'] = self.get_attr(element=_sum_room_count)
        summary_info['traveller_name'] = self.get_attr(element=_sum_traveller_name)
        summary_info['contact_info'] = self.get_attr(element=_sum_contact_info)
        return summary_info
