Feature: Attach Contact and Opportunity to Account

  Scenario: User attaches a contact and opportunity to an existing account
    Given I am logged into Salesforce
    When I create a contact for the existing account with company "ABC Bot" and name "Bot Test"
    Then I verify that the contact is attached to the account
    When I create an opportunity for the existing account with company "ABC Bot"
    Then I verify that the opportunity is attached to the account
