# pages/pg_Salesforce_Login.py
from selenium.webdriver.support import expected_conditions as EC
from pages.pg_base import BasePage
from pages.locators.pg_Salesforce_Locators import SalesforceLocators
from utils.logger import get_logger
from utils.selenium_utils import SeleniumUtils

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = SalesforceLocators()
        self.logger = get_logger()  # Get logger instance

    def get_locators(self):
        return self.locators

    def navigate_to_salesforce(self,base_url):
        """
        Navigates the WebDriver to Salesforce Login Page
        Prints the page title to the console after navigation.
        """
        SeleniumUtils.navigate(self.driver,base_url)
        self.logger.info("Navigation Success: " + SeleniumUtils.get_page_title(self.driver))

    def login_to_salesforce(self, username, password):
        """
        Login to Salesforce
        """
        # Wait until the username field is visible
        SeleniumUtils.enter_text(self.driver,self.locators.TXT_USERNAME,username)

        # Wait until the password field is visible
        SeleniumUtils.enter_text(self.driver,self.locators.TXT_PASSWORD,password)

        # Wait until the login button is visible and clickable
        SeleniumUtils.click(self.driver,self.locators.BTN_LOGIN)

        # Explicit wait for the page title to load after login
        SeleniumUtils.wait_for_condition(self.driver,EC.title_contains("Home"),60)
