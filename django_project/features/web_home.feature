Feature: Home Page
    In order to visit the site
    As a user
    I must have a home page

    Scenario: Anonymouse user visiting the home page
        Given I am not logged in
        When I visit the url 'web-home'
        Then I should get the status code '200'
        And I should see the template 'web/home.html'
