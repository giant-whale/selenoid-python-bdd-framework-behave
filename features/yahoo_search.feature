Feature: Yahoo Search Page contains weather results after opening from the main page

  Scenario Outline: Search City and find its weather in the results
    Given I open Yahoo main page
    When I input "<city_name> weather" and click Search
    Then There should be weather widget with the "<city_name>" in search results

    Examples: US
        | city_name       |
        | New York        |
        | Denver          |

    Examples: Germany
        | city_name       |
        | Berlin          |