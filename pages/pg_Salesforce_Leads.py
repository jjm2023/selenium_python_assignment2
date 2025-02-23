from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from pages.pg_base import BasePage
from pages.locators.pg_Salesforce_Locators import SalesforceLocators
from utils.logger import get_logger
from utils.selenium_utils import SeleniumUtils

class LeadsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = SalesforceLocators()
        self.logger = get_logger()  # Get logger instance

    def get_locators(self):
        return self.locators

    def navigate_to_menu_sales (self):
        SeleniumUtils.action_click(self.driver,self.locators.SPN_SALES)

    def navigate_to_new_leads_form(self):
        SeleniumUtils.action_click(self.driver, self.locators.DRP_LEADS)
        SeleniumUtils.action_click(self.driver, self.locators.LNK_NEW_LEAD)

    def enter_details_new_leads_form(self,salutation,firstname,lastname,company):
        try:
            SeleniumUtils.enter_text(self.driver, self.locators.TXT_SALUTATION, salutation)
            SeleniumUtils.enter_text(self.driver, self.locators.TXT_FIRST_NAME, firstname)
            SeleniumUtils.enter_text(self.driver, self.locators.TXT_LAST_NAME, lastname)
            SeleniumUtils.enter_text(self.driver, self.locators.TXT_COMPANY, company)
            SeleniumUtils.action_click(self.driver, self.locators.BTN_SAVE)
            SeleniumUtils.wait_for_condition(self.driver,EC.element_to_be_clickable(self.locators.BTN_CONVERT_LEAD))
        except Exception as e:
            self.logger.error(f"Failed to enter details for new leads form: {e}")

    def navigate_to_leads_home(self):
        SeleniumUtils.action_click(self.driver,self.locators.LNK_LEADS_HOME)

    def convert_lead_to_account(self,firstname,lastname):
        flag = 0
        try:
            SeleniumUtils.action_enter_text(self.driver, self.locators.TXT_SEARCH_ITEM, firstname + " " + lastname)
            SeleniumUtils.send_enter(self.driver, self.locators.TXT_SEARCH_ITEM)
            SeleniumUtils.wait_for_condition(self.driver, EC.element_to_be_clickable(self.locators.TXT_ACCOUNT_NAME),
                                             60)
            self.logger.info("Searching for existing lead")
            # Click on the search result if exists and navigate to the respective lead page
            title = SeleniumUtils.get_attribute(self.driver,self.locators.TXT_ACCOUNT_NAME,"title")
            if title and firstname in title:  # Check if the title contains firstname
                SeleniumUtils.action_click(self.driver,self.locators.TXT_ACCOUNT_NAME)
                SeleniumUtils.wait_for_condition(self.driver,EC.title_contains(firstname+" "+lastname+ " | Lead | Salesforce"),30)
                SeleniumUtils.action_click(self.driver,self.locators.BTN_CONVERT_LEAD)
                SeleniumUtils.action_click(self.driver,self.locators.BTN_SUBMIT_FORM_1)
                SeleniumUtils.action_click(self.driver,self.locators.BTN_SUBMIT_FORM_2)
                SeleniumUtils.clear_text(self.driver,self.locators.TXT_SEARCH_ITEM)
                SeleniumUtils.action_enter_text(self.driver, self.locators.TXT_SEARCH_ITEM,firstname+" "+lastname)
                SeleniumUtils.send_enter(self.driver, self.locators.TXT_SEARCH_ITEM)
                try:
                    SeleniumUtils.wait_for_condition(self.driver,EC.visibility_of_element_located(self.locators.TXT_ACCOUNT_NAME))
                    flag = 1
                except TimeoutException:
                    pass
            else:
                self.logger.error("No matching element found with the title containing " + firstname)
        except TimeoutException:
            self.logger.error("Timeout: No elements found within the given time.")
        except WebDriverException as e:
            self.logger.error(f"WebDriver error occurred: {e}")
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
        return flag




