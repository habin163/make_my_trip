import time
from selenium import webdriver

from src.main.Pages.HotelSearchResultPage import HotelSearchResultPage
from src.main.Pages.Hotels_Page import HotelsPage
from src.main.Pages.Navigation_Page import NavigationPage
from src.utils import constants


class Test_MMT:
    def test_search_hotels(self):
        driver = webdriver.Chrome("/Users/habinprasad/Experiments/Hackathons/make_my_trip/src/utils/driver_files"
                                  "/chromedriver")
        driver.get(constants.BASE_URL)
        hotels = HotelsPage(driver=driver)
        hotels.select_hotel()
        hotels.add_rooms()
        hotels.add_travelling_for()
        hotels.search_itenary()
        hotel_search_result = HotelSearchResultPage(driver=driver)
        hotel_search_result.add_room_filters()
        hotel_name = hotel_search_result.select_hotel_by_index()
        print(hotel_name)
        time.sleep(60)

