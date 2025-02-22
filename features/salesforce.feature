Feature: Verify Salesforce Login Functionality

  Background:
    Given the user navigates to the Salesforce login page

  Scenario: Successful login to Salesforce with valid credentials
    When the user enters valid credentials
    Then the user should be successfully logged in and see the 'Home | Salesforce' page


