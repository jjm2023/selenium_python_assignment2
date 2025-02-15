from behave import given, when, then
from pages.salesforce_pg import SalesforcePg
from utils.WebDriver import WebDriver

# Step 1: Login to Salesforce
@given('I am logged into Salesforce')
def step_impl(context):
    context.driver_instance = WebDriver()
    context.driver = context.driver_instance.initialize_driver()
    context.page = SalesforcePg(context.driver)
    context.page.login_to_salesforce(username="autotesterbot01-tj89@force.com", password="Qwerty@12345")

# Step 2: Create a new lead
@when('I create a new lead with first name "{firstname}" and last name "{lastname}"')
def step_impl(context, firstname, lastname):
    salutation = "Mr"
    company = "ABC"
    context.firstname_auto_code = context.page.create_new_lead(
        salutation=salutation, firstname=firstname, lastname=lastname, company=company)

# Step 3: Verify the Lead is Created
@then('I should see the lead "{firstname} {lastname}" in the lead list')
def step_impl(context, firstname, lastname):
    expected_title = f"{firstname} {context.firstname_auto_code} {lastname} | Lead | Salesforce"
    assert context.driver.title == expected_title, f"Expected title: {expected_title}, but got: {context.driver.title}"

# Step 4: Convert the Lead to Account
@when('I convert the lead "{firstname} {lastname}" to an account')
def step_impl(context, firstname, lastname):
    status = context.page.convert_an_existing_lead_to_account(firstname=f"{firstname}{context.firstname_auto_code}",
                                                               lastname=lastname)
    assert status == 0, f"Failed to convert lead {firstname} {lastname} to account."

@then('The lead should be successfully converted to an account')
def step_impl(context):
    # You can assert on some indicator that confirms the conversion to an account.
    # This may vary depending on your Salesforce implementation.
    pass
