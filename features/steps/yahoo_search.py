from behave import *

from pages.yahoo.yahoo_main_page import YahooMainPage
from pages.yahoo.yahoo_search_page import YahooSearchPage


@given('I open Yahoo main page')
def step_given_open_yahoo_main_page(context):
    context.yahoo_main_page = YahooMainPage().open()


@when('I input "{city_name} weather" and click Search')
def step__when_input_city_name_weather_and_search(context, city_name):
    context.yahoo_main_page.YahooSearchBar.search_input().input(city_name + ' weather')
    context.yahoo_main_page.YahooSearchBar.search_submit().click(wait_for_new_page=True)


@then('There should be weather widget with the "{city_name}" in search results')
def step_then_assert_correct_city_weather_in_result(context, city_name):
    assert YahooSearchPage().weather_widget_city_name().text == city_name
