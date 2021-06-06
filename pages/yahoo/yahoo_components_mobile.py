from core.locator import Locator


class YahooSearchBarMobile:
    search_fake_input = Locator('Search Fake Input', '//*[@id="header-search-button"]')
    search_input = Locator('Search Input', '//*[@id="header-search-form"]//input[@type="text"]')

    search_suggest_record = Locator('Search Result Record', '//*[@id="header-search-form"]//div[@type="normal"]//ul/li')

    def get_all_search_suggests(self):
        self.search_suggest_record().wait_for_element()
        return self.search_suggest_record.get_all_entities()
