import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.pg_Salesforce_Login import LoginPage
from pages.pg_Salesforce_Leads import LeadsPage
from utils.fileOps import FileOps
from utils.selenium_utils import SeleniumUtils
from utils.logger import get_logger
from pytest_bdd import scenario

# Read config values from the properties file
config = FileOps.read_config_properties()

# Load the scenarios from the feature file
featureFileDir = 'features'
featureFile = 'salesforce.feature'
scenarios('../' + featureFileDir + '/' + featureFile)

# set up logger
logger = get_logger()  # Get logger instance

@pytest.fixture(scope="session")
def random_number():
    """Generate a random number and return it for the session."""
    random_number = SeleniumUtils.generate_random_integer(100,999)
    return str(random_number)  # Return as string to append to names

@given("the user navigates to the Salesforce login page")
def navigate_to_salesforce(driver):
    LoginPage(driver).navigate_to_salesforce(config['base_url'])


@when("the user enters valid credentials")
def enter_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login_to_salesforce(config['username'], config['password'])


@then(parsers.parse("the user should be successfully logged in and see the {exp_page_title} page"))
def successful_login(driver, exp_page_title):
    # Remove the surrounding quotes if they exist in the expected page title
    exp_page_title = exp_page_title.strip("'")
    # Check if the page title contains the parameterized 'exp_page_title' after login
    assert exp_page_title in SeleniumUtils.get_page_title(driver)


@given("the user clicks on Sales menu")
def navigate_to_sales_menu(driver):
    leads_page = LeadsPage(driver)
    leads_page.navigate_to_menu_sales()


@when("the user navigates to New Lead Form")
def navigate_to_new_lead_form(driver):
    leads_page = LeadsPage(driver)
    leads_page.navigate_to_new_leads_form()


@then(parsers.parse("the user has entered {salutation}, {firstname}, {lastname}, {company} and saves"))
def enter_new_lead_form_and_save(driver, salutation, firstname, lastname, company, random_number):
    # Use the random_number passed from the fixture
    salutation = salutation.strip('"')
    firstname = firstname.strip('"')
    lastname = lastname.strip('"')
    company = company.strip('"')

    # Modify firstname to include the random number
    firstname = f"{firstname}_{random_number}"

    leads_page = LeadsPage(driver)
    leads_page.enter_details_new_leads_form(salutation=salutation, firstname=firstname, lastname=lastname,
                                            company=company)


@then(parsers.parse("the user navigates to lead home page to convert new lead with {firstname}, {lastname} as account"))
def convert_lead_to_account(random_number, driver, firstname, lastname):
    firstname = firstname.strip('"')
    lastname = lastname.strip('"')

    # Use the random_number passed from the fixture
    if not random_number:
        raise AssertionError("Random number was not generated correctly!")

    # Modify firstname to include the random number
    firstname = f"{firstname}_{random_number}"

    leads_page = LeadsPage(driver)
    leads_page.navigate_to_leads_home()
    status = leads_page.convert_lead_to_account(firstname=firstname, lastname=lastname)

    if status != 0:
        raise AssertionError(f"Assertion failed! Lead conversion to Account failed for {firstname}")
