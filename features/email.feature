Feature: Email

  Scenario: Login into the gmail
    Given I am already registered to the email website
    And I am on the login page
    And Cookies dialog pops up
    When I have accepted cookies
    Then Cookies dialog closes

    When I have clicked login button
    Then I should be redirected to login page

    When I have entered <username> into "username" field
    And I have entered <password> into "password" field
    And I pressed the "log in" button
    Then I should be logged in and redirected to my email inbox

  Scenario: Creating and sending email to addressee from contacts with file attachment
    Given I am logged in and I'm in my inbox
    When I click on "write e-mail" button
    Then Window with email form is opened

    When I fill out addressee of mail
    Then addressee of mail should be filled out

    When I fill out topic of mail
    Then topic of mail should be filled out

    When I fill out body of mail
    Then body of mail should be filled out

    When I attach a file
    Then file should be attached

    When I click on send email
    Then Mail should be sent to addressee

  Scenario: Log out from the email
    Given I am logged in into the system

    When I click my avatar in top right corner
    Then Drop-down menu is opened

    When I click log out
    Then I should be logged out from email