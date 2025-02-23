Feature: Verify Salesforce Login Functionality

  Background:
    Given the user navigates to the Salesforce login page
    When the user enters valid credentials
    Then the user should be successfully logged in and see the 'Home | Salesforce' page

  Scenario Outline: Create a Lead and convert that to Account from Lead's Page
    Given the user clicks on Sales menu
    When the user navigates to New Lead Form
    Then the user has entered "<Salutation>", "<First Name>", "<Last Name>", "<Company>" and saves
    And the user navigates to lead home page to convert new lead with "<First Name>", "<Last Name>" as account

  Examples:
    | Salutation | First Name | Last Name | Company     |
    | Mr.        | Autotester | test      | Test Corp   |




