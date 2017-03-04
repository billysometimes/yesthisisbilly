Feature: Viewing blog

  Scenario: I view a list of posts
    Given there is a list of posts
    |   title     |   slug        |   author    |   body    |
    | First Post  |   First Slug  |   webby     | body 1    |
    | 2 post      |   2 slug      |   webby     | b2        |
    | 3           |   3 slug      |   webby     | bod       |
    | 4           |   4           |   webby     | a         |
    | 5           |   5           |   webby     | a         |
    | 6           |   6           |   webby     | a         |
    When I visit the url "/blog"
    Then I see a list of 5 posts
