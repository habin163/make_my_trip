"""
This consists of actions handling Hotel Search Results Page
"""
import time

from src.main.Pages.Hotels_Page import HotelsPage
from src.utils import constants

_div_overlay = "//div[@class='mmBackdrop wholeBlack']"
_slider_lower_end = "//div[@id='hlistpg_fr_price_per_night']//span[1]//div[@class='input-range__slider']"
_span_slider_max_value = "//span[@class='maxValue']"  # Write logic to convert minimum to %age via x/30000
_label_user_rating = "//label[contains(text(),'{}')]"  # 4 & above (Very Good)
_div_hotel_listed = "//div[@id='Listing_hotel_{}']"  # 4 for 5th hotel
_span_hotel_name = "//div[@id='Listing_hotel_{}']//span[starts-with(@id,'htl_id_')]"  # 4 for 5th hotel
_li_rooms_nav = "//a[@id='detpg_hotel_rooms']"
_div_room_indexed = "//div[@class='roomWrap'][{}]"  # 1 for first room category
_select_button = "//div[contains(@class,'recRoom')]//a[contains(.,'SELECT')]"
_room_info_ = "//div[@class='roomWrap'][{}]//ul[starts-with(@class,'append')]/li"  # 1 for first room category


class HotelSearchResultPage(HotelsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_room_filters(self, min_cost: int = 1000, user_rating: str = '4 & above (Very Good)'):
        self.utils.clear_overlay(element=_div_overlay)
        time.sleep(constants.SCROLL_VIEWPORT_WAIT)
        self.utils.bring_element_in_viewport(element=_span_slider_max_value)
        room_rent_max = int(self.utils.get_elem_attr(element=_span_slider_max_value).replace("INR ", ""))
        y_offset = float(min_cost * 200 / room_rent_max)
        self.utils.slider_action(element=_slider_lower_end, h_value=y_offset)
        time.sleep(constants.SCROLL_VIEWPORT_WAIT)
        user_rated_element = _label_user_rating.format(user_rating)
        self.utils.bring_element_in_viewport(element=user_rated_element)
        self.clicks(element=user_rated_element)

    def select_hotel_by_index(self, hotel_index: int = 5):
        hotel_index = hotel_index - 1
        hotel_name = self.utils.get_elem_attr(element=_span_hotel_name.format(hotel_index))
        self.clicks(element=_span_hotel_name.format(hotel_index))
        return hotel_name

    def rooms_selection(self):
        self.utils.bring_element_in_viewport(element=_li_rooms_nav)
        room_info_list = self.capture_room_info()
        self.clicks(element=_select_button)
        return room_info_list

    def capture_room_info(self, room_index=1):
        infos = self.driver.find_elements_by_xpath(_room_info_.format(room_index))
        room_info_list = []
        for info in infos:
            room_info_list.append(info.get_attribute('innerText'))
        return room_info_list

