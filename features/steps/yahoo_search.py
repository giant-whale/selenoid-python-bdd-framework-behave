from behave import *

from pages.yahoo.yahoo_main_page import YahooMainPage
from pages.yahoo.yahoo_main_page_mobile import YahooMainPageMobile
from pages.yahoo.yahoo_search_page import YahooSearchPage


@given('I open Yahoo main page')
def step_given_open_yahoo_main_page(context):
    if context.is_mobile:
        context.yahoo_main_page = YahooMainPageMobile().open()
    else:
        context.yahoo_main_page = YahooMainPage().open()


@when('I input "{city_name} weather" and click Search')
def step_when_input_city_name_weather_and_search(context, city_name):
    context.yahoo_main_page.YahooSearchBar.search_input().input(city_name + ' weather')
    context.yahoo_main_page.YahooSearchBar.search_submit().click(wait_for_new_page=True)


@when('I click on fake search input and input "{query}"')
def step_when_mobile_input_into_search(context, query):
    context.query = query
    context.yahoo_main_page.YahooSearchBarMobile.search_fake_input().click()
    context.yahoo_main_page.YahooSearchBarMobile.search_input().input(query)


@then('There should be search suggests with query in it\'s text')
def step_then_assert_suggests_contains_query_string(context):
    suggests = context.yahoo_main_page.YahooSearchBarMobile.get_all_search_suggests()
    for suggest in suggests:
        assert context.query in suggest.text


@then('There should be weather widget with the "{city_name}" in search results')
def step_then_assert_correct_city_weather_in_result(context, city_name):
    assert YahooSearchPage().weather_widget_city_name().text == city_name
