from behave import given, when, then
from pages.salesforce_pg import SalesforcePg
from utils.WebDriver import WebDriver

# Step 1: Create a Contact for the Account
@when('I attach a contact to the account with company name "{companyname}"')
def step_impl(context, companyname):
    status = context.page.create_contact_for_existing_account(companyname=companyname,
                                                               firstname="Bot", lastname="Test")
    assert status == 0, f"Failed to create contact for the account with company name {companyname}."

# Step 2: Verify Contact is Successfully Attached to the Account
@then('I should see the contact attached to the account "{companyname}"')
def step_impl(context, companyname):
    # You can assert by checking for the presence of the contact in the account details.
    pass

# Step 3: Attach an Opportunity to the Account
@when('I attach an opportunity to the account with company name "{companyname}"')
def step_impl(context, companyname):
    status = context.page.create_opportunity_for_existing_account(companyname=companyname)
    assert status == 0, f"Failed to create opportunity for the account with company name {companyname}."

# Step 4: Verify Opportunity is Successfully Attached to the Account
@then('I should see the opportunity attached to the account "{companyname}"')
def step_impl(context, companyname):
    # You can assert by checking for the presence of the opportunity in the account details.
    pass
