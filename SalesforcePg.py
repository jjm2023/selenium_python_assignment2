import random

from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from BasePg import BasePg
from SalesforceLocators import SalesforceLocators
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import time

""" This is the Page Class - Salesforce App """


class SalesforcePg(BasePg):
    def __init__(self, driver):
        super().__init__(driver)

    def get_locator(self):
        # Here we return locators from the SalesforceLocators class
        return SalesforceLocators

    def wait_until_visible(self, locator, timeout=30):
        """
        Waits for an element to become visible within the specified timeout.
        """
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def navigate_to_salesforce(self):
        """
        Navigates the WebDriver to Salesforce Login Page
        Prints the page title to the console after navigation.
        """
        self.driver.get("https://ability-energy-5933.my.salesforce.com/")
        # print("Navigation Success: " + self.driver.title)

    def login_to_salesforce(self, username, password):
        """
        Login to Salesforce
        """
        self.navigate_to_salesforce()

        # Wait until the username field is visible
        username_field = self.wait_until_visible(self.get_locator().TXT_USERNAME)
        username_field.send_keys(username)

        # Wait until the password field is visible
        password_field = self.wait_until_visible(self.get_locator().TXT_PASSWORD)
        password_field.send_keys(password)

        # Wait until the login button is visible and clickable
        login_button = self.wait_until_visible(self.get_locator().BTN_LOGIN)
        login_button.click()

        # Set an implicit wait time of 10 seconds
        self.driver.implicitly_wait(10)
        time.sleep(15)

    def create_new_lead(self, salutation, firstname, lastname, company):
        """
        Create a new lead by filling out the necessary fields
        """
        # Generate a dynamic 3-digit integer
        random_three_digit_integer = random.randint(100, 999)

        # Wait and click on Sales span
        sales_span = self.wait_until_visible(self.get_locator().SPN_SALES)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(sales_span).perform()
        # sales_span.click()

        # Wait and click on the Leads dropdown
        leads_dropdown = self.wait_until_visible(self.get_locator().DRP_LEADS)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(leads_dropdown).perform()
        # leads_dropdown.click()

        # Wait and click on New Lead link
        new_lead_link = self.wait_until_visible(self.get_locator().LNK_NEW_LEAD)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(new_lead_link).perform()
        # new_lead_link.click()

        # Wait and fill in the Salutation field
        salutation_field = self.wait_until_visible(self.get_locator().TXT_SALUTATION)
        salutation_field.send_keys(salutation)

        # Wait and fill in the First Name field
        first_name_field = self.wait_until_visible(self.get_locator().TXT_FIRST_NAME)
        temp = str(random_three_digit_integer)
        first_name_field.send_keys(firstname + temp)

        # Wait and fill in the Last Name field
        last_name_field = self.wait_until_visible(self.get_locator().TXT_LAST_NAME)
        last_name_field.send_keys(lastname)

        # Wait and fill in the Company field
        company_field = self.wait_until_visible(self.get_locator().TXT_COMPANY)
        company_field.send_keys(company + temp)

        # Wait and click on the Save button
        save_button = self.wait_until_visible(self.get_locator().BTN_SAVE)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(save_button).perform()
        # save_button.click()
        # print("Create Lead - Complete for " + firstname + temp)

        # Wait until visible
        save_button = self.wait_until_visible(self.get_locator().BTN_CONVERT_LEAD)

        return temp

    def convert_an_existing_lead_to_account(self, firstname, lastname):
        """
        Convert a lead to an account
        """
        flag = 0

        # Wait and click on Leads link
        lnk_leads_home = self.wait_until_visible(self.get_locator().LNK_LEADS_HOME)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(lnk_leads_home).perform()

        # Wait and pass search input for the lead
        txt_search = self.wait_until_visible(self.get_locator().TXT_SEARCH_ITEM)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(txt_search).send_keys(firstname + " " + lastname).send_keys(Keys.ENTER).perform()
        # Sleep for 15 seconds
        time.sleep(15)

        # Click on the search result if exists and navigate to the respective lead page
        try:
            txt_account_name = self.wait_until_visible(self.get_locator().TXT_ACCOUNT_NAME)
            # Get the 'title' attribute of the element
            title = txt_account_name.get_attribute("title")
            if title and firstname in title:  # Check if the title contains firstname
                txt_account_name.click()  # Click on the element
                # print(f"Clicked on element with title: {title}")
                # Wait for the new page to load and check its title
                WebDriverWait(self.driver, 10).until(
                    ec.title_contains(firstname + " " + lastname + " | Lead | Salesforce"))
                # print("New page loaded with title containing " + firstname + " " + lastname + " | Lead | Salesforce")
                # Wait and click on Convert button
                btn_convert_lead = self.wait_until_visible(self.get_locator().BTN_CONVERT_LEAD)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.click(btn_convert_lead).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Wait and click on Convert Button
                # self.wait_until_visible(self.get_locator().MSG_CONVERT_SUCCESS)
                btn_convert_confirm = self.wait_until_visible(self.get_locator().BTN_SUBMIT_FORM_1)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.click(btn_convert_confirm).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Wait and click on Go to Leads Button
                # self.wait_until_visible(self.get_locator().MSG_CONVERT_SUCCESS)
                btn_goto_leads = self.wait_until_visible(self.get_locator().BTN_SUBMIT_FORM_2)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.click(btn_goto_leads).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Wait and pass search input for the lead
                txt_search = self.wait_until_visible(self.get_locator().TXT_SEARCH_ITEM)
                txt_search.clear()
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                # First, click the input field, clear the existing text, and send new text
                # actions.click(txt_search).send_keys(Keys.CONTROL + "a")  # Select all text
                # actions.send_keys(Keys.BACKSPACE)  # Clear the selected text
                actions.send_keys(firstname + " " + lastname)  # Enter new text
                actions.send_keys(Keys.ENTER)  # Press Enter
                actions.perform()
                # Sleep for 15 seconds
                time.sleep(15)
                try:
                    txt_account_name = self.wait_until_visible(self.get_locator().TXT_ACCOUNT_NAME)
                    flag = 1
                except TimeoutException:
                    pass
            else:
                print("No matching element found with the title containing " + firstname)

        except TimeoutException:
            print("Timeout: No elements found within the given time 1.")
        except WebDriverException as e:
            print(f"WebDriver error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return flag

    def create_contact_for_existing_account(self, companyname, firstname, lastname):
        """
        Create a contact for existing account
        """
        flag = 0

        # Wait and click on Accounts link
        lnk_accounts_home = self.wait_until_visible(self.get_locator().LNK_ACCOUNTS_HOME)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(lnk_accounts_home).perform()
        # Sleep for 15 seconds
        time.sleep(15)

        # Wait and pass search input for the lead
        txt_search = self.wait_until_visible(self.get_locator().TXT_SEARCH_ITEM)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(txt_search).click(txt_search).send_keys(companyname).send_keys(Keys.ENTER).perform()
        # Sleep for 15 seconds
        time.sleep(15)

        # Click on the search result if exists and navigate to the respective accounts page
        try:
            txt_account_name = self.wait_until_visible(self.get_locator().TXT_ACCOUNT_NAME)
            # Get the 'title' attribute of the element
            title = txt_account_name.get_attribute("title")
            if title and companyname in title:  # Check if the title contains firstname
                txt_account_name.click()  # Click on the element
                # print(f"Clicked on element with title: {title}")
                # Wait for the new page to load and check its title
                WebDriverWait(self.driver, 10).until(
                    ec.title_contains(companyname + " | Account | Salesforce"))
                # Sleep for 15 seconds
                time.sleep(15)
                # print("New page loaded with title containing " + companyname + " | Account | Salesforce")
                # Wait and click on New Contact button
                btn_new_contact = self.wait_until_visible(self.get_locator().BTN_NEW_CONTACT_FOR_ACCOUNT)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.move_to_element(btn_new_contact).click(btn_new_contact).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Generate a dynamic 4-digit integer
                random_four_digit_integer = random.randint(1000, 9999)
                # Wait and fill in the First Name field
                first_name_field = self.wait_until_visible(self.get_locator().TXT_FIRST_NAME)
                temp = str(random_four_digit_integer)
                first_name_field.send_keys(firstname + temp)
                # Wait and fill in the Last Name field
                last_name_field = self.wait_until_visible(self.get_locator().TXT_LAST_NAME)
                last_name_field.send_keys(lastname)
                # Wait and save the contact
                btn_save_new_contact = self.wait_until_visible(self.get_locator().BTN_SAVE_NEW_CONTACT)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.click(btn_save_new_contact).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Wait and click on Contacts Home
                lnk_contact_home = self.wait_until_visible(self.get_locator().LNK_CONTACT_HOME)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.click(lnk_contact_home).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Wait and pass search input for the contact
                txt_search = self.wait_until_visible(self.get_locator().TXT_SEARCH_ITEM)
                txt_search.clear()
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.move_to_element(txt_search)
                actions.click(txt_search)
                actions.send_keys(firstname + temp)  # Enter new text
                actions.send_keys(Keys.ENTER)  # Press Enter
                actions.perform()
                # Sleep for 15 seconds
                time.sleep(15)
                try:
                    txt_contact_name = self.wait_until_visible(self.get_locator().TXT_ACCOUNT_NAME)
                    txt_account_name = self.wait_until_visible(self.get_locator().TXT_COMPANY_NAME)
                    if txt_contact_name.get_attribute('title') == firstname + temp + " " + lastname:
                        if txt_account_name.get_attribute('title') == companyname:
                            pass
                    else:
                        flag = 1
                except TimeoutException:
                    flag = 1
            else:
                print("No matching element found with the title containing " + firstname)

        except TimeoutException:
            print("Timeout: No elements found within the given time 1.")
        except WebDriverException as e:
            print(f"WebDriver error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return flag

    def create_opportunity_for_existing_account(self, companyname):
        """
        Create a opportunity for existing account
        """
        flag = 0

        # Wait and click on Accounts link
        lnk_accounts_home = self.wait_until_visible(self.get_locator().LNK_ACCOUNTS_HOME)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.click(lnk_accounts_home).perform()
        # Sleep for 15 seconds
        time.sleep(15)

        # Wait and pass search input for the lead
        txt_search = self.wait_until_visible(self.get_locator().TXT_SEARCH_ITEM)
        # Perform a click using ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(txt_search).click(txt_search).send_keys(companyname).send_keys(Keys.ENTER).perform()
        # Sleep for 15 seconds
        time.sleep(15)

        # Click on the search result if exists and navigate to the respective accounts page
        try:
            txt_account_name = self.wait_until_visible(self.get_locator().TXT_ACCOUNT_NAME)
            # Get the 'title' attribute of the element
            title = txt_account_name.get_attribute("title")
            if title and companyname in title:  # Check if the title contains firstname
                txt_account_name.click()  # Click on the element
                # print(f"Clicked on element with title: {title}")
                # Wait for the new page to load and check its title
                WebDriverWait(self.driver, 10).until(
                    ec.title_contains(companyname + " | Account | Salesforce"))
                # Sleep for 15 seconds
                time.sleep(15)
                # print("New page loaded with title containing " + companyname + " | Account | Salesforce")
                # Wait and click on New Contact button
                btn_new_opportunity = self.wait_until_visible(self.get_locator().BTN_NEW_OPPORTUNITY_FOR_ACCOUNT)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.move_to_element(btn_new_opportunity).click(btn_new_opportunity).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Generate a dynamic 4-digit integer
                random_four_digit_integer = random.randint(1000, 9999)
                # Wait and fill in the Opportunity Name field
                opportunity_name_field = self.wait_until_visible(self.get_locator().TXT_OPPORTUNITY_NAME)
                temp = str(random_four_digit_integer)
                opportunity_name_field.clear()
                opportunity_name_field.send_keys("OPP" + temp)
                # Wait and save the opportunity
                btn_save_new_opportunity = self.wait_until_visible(self.get_locator().BTN_SAVE_NEW_OPPORTUNITY)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.click(btn_save_new_opportunity).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Wait and click on Opportunities Home
                lnk_opportunity_home = self.wait_until_visible(self.get_locator().LNK_OPPORTUNITIES_HOME)
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.click(lnk_opportunity_home).perform()
                # Sleep for 15 seconds
                time.sleep(15)
                # Wait and pass search input for the contact
                txt_search = self.wait_until_visible(self.get_locator().TXT_SEARCH_ITEM)
                txt_search.clear()
                # Perform a click using ActionChains
                actions = ActionChains(self.driver)
                actions.move_to_element(txt_search)
                actions.click(txt_search)
                actions.send_keys("OPP" + temp)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                # Sleep for 15 seconds
                time.sleep(15)
                try:
                    txt_opportunity_name = self.wait_until_visible(self.get_locator().TXT_ACCOUNT_NAME)
                    txt_account_name = self.wait_until_visible(self.get_locator().TXT_COMPANY_NAME)
                    if txt_opportunity_name.get_attribute('title') == "OPP" + temp:
                        if txt_account_name.get_attribute('title') == companyname:
                            pass
                    else:
                        flag = 1
                except TimeoutException:
                    flag = 1
            else:
                print("No matching element found with the title containing " + companyname)

        except TimeoutException:
            print("Timeout: No elements found within the given time 1.")
        except WebDriverException as e:
            print(f"WebDriver error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return flag
