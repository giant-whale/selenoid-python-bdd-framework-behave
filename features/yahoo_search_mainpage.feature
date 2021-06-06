Feature: Mobile - Yahoo Main Page contains suggests in search input related to query

  Scenario Outline: Search word and look in result if all the results contains query string
    Given I open Yahoo main page
    When I click on fake search input and input "<query>"
    Then There should be search suggests with query in it's text

    Examples: Single Word
        | query   |
        | banana  |
        | apple   |

    Examples: Multiple Words
        | query           |
        | random string   |