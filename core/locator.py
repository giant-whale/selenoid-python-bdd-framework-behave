from selenium.common.exceptions import (
    InvalidSelectorException,
    NoSuchElementException,
)
from selenium.webdriver.support.wait import WebDriverWait

from core.driver import Driver
from core.exceptions import CustomBrokenException
from core.helpers import (
    wait_for_page_to_change,
    wait_for_page_to_load,
)


class Locator:
    """
    Present locators on pages
    """
    xpath = None
    webelement = None
    name = None

    def __init__(self, name: str, xpath: str, webelement=None):
        self.xpath = xpath
        self.name = name
        self.webelement = webelement

    def __call__(self):
        try:
            self.webelement = Driver().find_element_by_xpath(self.xpath)
            return self
        except (InvalidSelectorException, NoSuchElementException):
            raise CustomBrokenException(f'Error: cannot locate {self.name}')

    def click(self, wait_for_new_page: bool = False):
        if wait_for_new_page:
            Driver().execute_script('var oldPage = 1;')
            self.webelement.click()
            wait_for_page_to_change()
            wait_for_page_to_load()
        else:
            self.webelement.click()

    def input(self, string: str):
        self.webelement.send_keys(string)

    def is_on_page(self) -> bool:
        return self.webelement.is_displayed()

    def wait_for_element(self, wait_time=5):
        WebDriverWait(Driver, wait_time).until(lambda x: x.find_element_by_xpath(self.webelement, self.xpath).is_displayed())

    @property
    def text(self):
        return self.webelement.text

    def get_all_entities(self):
        webelements = Driver().find_elements_by_xpath(self.xpath)
        locators = []
        for webelement in webelements:
            locators.append(Locator(name=self.name, xpath=self.xpath, webelement=webelement))
        return locators
