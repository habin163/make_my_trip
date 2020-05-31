import pytest
from selenium import webdriver

from src.main.Pages.BookingPage import BookingPage
from src.main.Pages.BookingSummary import BookingSummary
from src.main.Pages.HotelSearchResultPage import HotelSearchResultPage
from src.main.Pages.Hotels_Page import HotelsPage
from src.utils import constants


def pytest_configure(config):
    """ remove unwanted env """
    config._metadata.pop('Packages')
    config._metadata.pop('Platform')
    config._metadata.pop('Plugins')
    config._metadata.pop('Python')
    metadata_dict = {'NODE_NAME': '', 'Machine': '', 'JOB_NAME': '',
                     'WORKSPACE': '',
                     'BUILD_TAG': '', 'EXECUTOR_NUMBER': '',
                     'BUILD_URL': '',
                     'JENKINS_URL': '',
                     'GIT_COMMIT': '', 'JAVA_HOME': '',
                     'Code/Branch': '', 'BUILD_NUMBER': '', 'GIT_BRANCH': '',
                     'GIT_URL': '', 'BUILD_ID': ''}
    for env in metadata_dict:
        if env in config._metadata:
            config._metadata.pop(env)
    config._metadata['Test URL'] = getattr(config, '_branch', constants.BASE_URL)


def pytest_collectreport(report):
    """For handling collection related errors"""
    if report.failed:
        raise pytest.UsageError("Errors during collection, aborting")


@pytest.fixture(scope="session")
def test_setup_(pytestconfig):
    _setup = dict()
    driver = webdriver.Chrome("/Users/habinprasad/Experiments/Hackathons/make_my_trip/src/utils/driver_files"
                              "/chromedriver")
    driver.maximize_window()
    driver.get(constants.BASE_URL)
    _setup['driver'] = driver
    _setup['hotels'] = HotelsPage(driver=driver)
    _setup['hotel_search_result'] = HotelSearchResultPage(driver=driver)
    _setup['booking_page'] = BookingPage(driver=driver)
    _setup['booking_summ'] = BookingSummary(driver=driver)
    return _setup