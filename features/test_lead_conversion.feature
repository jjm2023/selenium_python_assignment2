Feature: Salesforce Lead Creation and Conversion
  As a user
  I want to create a lead and convert it into an account
  So that I can verify the entire lead-to-account process in Salesforce

  Scenario: Create and Convert Lead to Account
    Given I log in to Salesforce
    When I create a lead with name "Bot Test" and company "ABC"
    Then I should see the lead with name "Bot Test" and company "ABC" in the system
    When I convert the lead to an account
    Then I should see the account "Bot Test ABC" in the system
