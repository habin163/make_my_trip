"""
Handles all the activities for Booking Page
"""

from src.main.Pages.Navigation_Page import NavigationPage
from src.utils import constants

_input_first_name = "//input[@id='fName']"
_input_last_name = "//input[@id='lName']"
_input_mobile_no = "//input[@id='mNo']"
_list_commonly_requested = "//div[@class='_SpecialRequest']//label"
_label_commonly_requested = _list_commonly_requested + "[@for='10{}']"  # elements
_mmt_donation = "//label[@for='donation']"
_pay_now = "//a[@class='primaryBtn btnPayNow']"


class BookingPage(NavigationPage):
    def __init__(self, driver):
        super().__init__(driver)

    def __add_random_common_request(self, count=2):
        commonly_requested_count = len(self.driver.find_elements_by_xpath(_label_commonly_requested))
        count = count if count < commonly_requested_count else commonly_requested_count
        rnd_req_list = []
        for i in range(count):
            _elem = _label_commonly_requested.format(i + 1)
            self.clicks(element=_elem)
            rnd_req_list.append(self.utils.get_elem_attr(element=_elem))
        return rnd_req_list

    def enter_booking_details_and_pay(self, first_name=constants.F_NAME, last_name=constants.L_NAME,
                                      contact_no=constants.CONTACT, common_req=2):
        self.inputs(element=_input_first_name, text=first_name)
        self.inputs(element=_input_last_name, text=last_name)
        self.inputs(element=_input_mobile_no, text=contact_no)
        special_requests = self.__add_random_common_request(common_req)
        self.clicks(element=_mmt_donation)
        self.clicks(element=_pay_now)
        self.utils.wait_()
        return special_requests


