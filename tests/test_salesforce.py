from pytest_bdd import scenarios, given, when, then, parsers
from pages.pg_Salesforce_Login import LoginPage
from utils.fileOps import FileOps
from utils.selenium_utils import SeleniumUtils
from utils.logger import get_logger

# Read config values from the properties file
config = FileOps.read_config_properties()

# Load the scenarios from the feature file
featureFileDir = 'features'
featureFile = 'salesforce.feature'
scenarios('../'+featureFileDir+'/'+featureFile)

logger = get_logger()  # Get logger instance

# This step is for the Background part to navigate to the Salesforce login page
@given("the user navigates to the Salesforce login page")
def navigate_to_salesforce(driver):
    LoginPage(driver).navigate_to_salesforce(config['base_url'])

# This step corresponds to the "When the user enters valid credentials"
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