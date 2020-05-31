import time


class Test_MMT:
    def test_search_hotels(self, test_setup_):
        driver = test_setup_['driver']
        hotels = test_setup_['hotels']
        hotels.select_hotel()
        hotels.add_rooms()
        hotels.add_travelling_for()
        hotels.search_itenary()
        hotel_search_result = test_setup_['hotel_search_result']
        hotel_search_result.add_room_filters()
        hotel_name = hotel_search_result.select_hotel_by_index()
        print(hotel_name)
        time.sleep(60)
        room_info_list = hotel_search_result.rooms_selection()
        print(room_info_list)
        booking_page = test_setup_['booking_page']
        commonly_requested = booking_page.enter_booking_details_and_pay()
        print(commonly_requested)
        booking_summ = test_setup_['booking_summ']
        booking_summ.fetch_summary_values()
        driver.quit()
