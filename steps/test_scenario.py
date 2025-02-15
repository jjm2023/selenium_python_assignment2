# test_scenario.py
import pytest
from pytest_bdd import given, when, then
from utils.config import read_config
from pages.salesforce_pg import SalesforcePg

# Load configuration values
config = read_config()

# Initialize Page object
@pytest.fixture
def page(driver):
    return SalesforcePg(driver)

@given('I log in to Salesforce')
def step_impl_login(page):
    username = config['salesforce']['username']
    password = config['salesforce']['password']
    page.login_to_salesforce(username, password)

@when('I create a lead with name "{name}" and company "{company}"')
def step_impl_create_lead(page, name, company):
    salutation = "Mr"
    firstname, lastname = name.split()
    page.create_new_lead(salutation=salutation, firstname=firstname, lastname=lastname, company=company)

@then('I should see the lead with name "{name}" and company "{company}" in the system')
def step_impl_verify_lead(driver, name, company):
    firstname, lastname = name.split()
    lead_title = f"{firstname} {lastname} | Lead | Salesforce"
    assert driver.title == lead_title, f"Expected title '{lead_title}', but got '{driver.title}'."

@when('I convert the lead to an account')
def step_impl_convert_lead(page):
    firstname = "Bot"
    lastname = "Test"
    page.convert_an_existing_lead_to_account(firstname=firstname, lastname=lastname)

@then('I should see the account "{account_name}" in the system')
def step_impl_verify_account(driver, account_name):
    account_title = f"{account_name} | Account | Salesforce"
    assert driver.title == account_title, f"Expected title '{account_title}', but got '{driver.title}'."
