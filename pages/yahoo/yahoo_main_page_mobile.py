from core.locator import Locator
from core.page import Page

from pages.yahoo.yahoo_components_mobile import YahooSearchBarMobile


class YahooMainPageMobile(Page):
    BASE_PAGE_URL = "https://www.yahoo.com/"

    menu_button = Locator('Menu Button', '//*[@id="header-profile-button"]')
    menu_popup = Locator('Menu Popup', '//*[@id="header-overlay"]')

    @staticmethod
    def is_menu_displayed():
        # page adds "profile-open" class to Body, this is the only way to check if menu is displayed
        opened_menu_class = "profile-open"
        body = Locator('Page Body with opened menu', '//body')
        body_classes = body().webelement.get_attribute('class')
        if opened_menu_class in body_classes:
            return True
        else:
            return False

    YahooSearchBarMobile = YahooSearchBarMobile()
