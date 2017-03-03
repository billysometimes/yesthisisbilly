Feature: Show blog
  As a standard user
  I want to view the blog
  So I can see a list of blog posts

  Background: There are blog posts
    Given there are a number of posts in the database

  Scenario: Visit blog page
    Given I an a standard user
    And I access the url "/blog"
    Then I see a list of  posts
