Feature: Verify Salesforce Login Functionality

  Background:
    Given the user navigates to the Salesforce login page
    When the user enters valid credentials
    Then the user should be successfully logged in and see the 'Home | Salesforce' page

  @usecase1
  Scenario Outline: Create a Lead and convert that to Account from Lead's Page
    Given the user clicks on Sales menu
    When the user navigates to New Lead Form
    Then the user has entered "<Salutation>", "<First Name>", "<Last Name>", "<Company>" and saves
    And the user navigates to lead home page to convert new lead with "<First Name>", "<Last Name>" as account

  Examples:
    | Salutation | First Name | Last Name | Company     |
    | Mr.        | Autotester | Test      | Test Corp   |

  @usecase2
  Scenario Outline: Create an account and attach contact and opportunity
    Given the user clicks on Sales menu
    When the user navigates to New Lead Form
    Then the user has entered "<Salutation>", "<First Name>", "<Last Name>", "<Company>" and saves
    And the user navigates to lead home page to convert new lead with "<First Name>", "<Last Name>" as account
    Then the user attaches a contact to the account "<First Name>", "<Last Name>", "<Company>" as "<Contact Name>"
    And the user attaches an opportunity to the account "<Company>" as "<Opportunity Name>"

  Examples:
    | Salutation | First Name | Last Name | Company    | Contact Name | Opportunity Name |
    | Mrs.       | Autobot    | Test      | Test Inc   | Bot          | ABC-Opportunity  |

