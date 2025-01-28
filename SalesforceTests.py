from SalesforcePg import SalesforcePg
from WebDriver import WebDriver

""" This is the Test Class - Salesforce App """
class SalesforceTests:
    def __init__(self):
        self.driver_instance = WebDriver()
        self.driver = None
        self.page = None

    def run_test(self):
        # Step 1: Initialize WebDriver
        self.driver = self.driver_instance.initialize_driver()

        # Step 2: Initialize Page
        self.page = SalesforcePg(self.driver)

        # Step 3: Initialize Test Data
        username = ""
        password = ""
        salutation = "Mr"
        firstname = "Bot"
        lastname = "Test"
        company = "ABC"

        print("~~~~ Running Test - " + "Use case-1 :  Create a lead and convert that to an account from Lead Page.")

        # Step 1: Login
        exp_title = "Lightning Experience"
        self.page.login_to_salesforce(username=username, password=password)
        if self.driver.title == exp_title:
            print("Step:Login- Pass")
        else:
            print("Step:Login- Fail")

        # Step 2: Create Lead
        firstname_auto_code = self.page.create_new_lead(salutation=salutation, firstname=firstname, lastname=lastname,
                                                        company=company)
        exp_title = firstname + firstname_auto_code + " " + lastname + " | Lead | Salesforce"
        if self.driver.title == exp_title:
            print("Step:Create Lead- Pass " + "Actual - " + self.driver.title)
        else:
            print("Actual Title - " + self.driver.title)
            print("Step:Create Lead- Fail " + "Expected - " + exp_title)

        # Step 3: Verify Created Lead can be converted to an Account
        status = self.page.convert_an_existing_lead_to_account(firstname=firstname + firstname_auto_code,
                                                               lastname=lastname)
        if status == 0:
            print("Test:Convert Lead to Account - Pass ")
        else:
            print("Test:Convert Lead to Account - Fail ")

        print("XXXX END OF TEST XXXX")

        print("~~~~ Running Test - " + "Use case -2 : For Existing Account , attach contact and opportunity object to the account.")

        # Step 4: Verify Created Account can attach a new contact
        status = self.page.create_contact_for_existing_account(companyname=company + firstname_auto_code, firstname=firstname,
                                                               lastname=lastname)
        if status == 0:
            print("Test:Attach Contact to Account - Pass ")
        else:
            print("Test:Attach Contact to Account - Fail ")

        # Step 5: Verify Created Account can attach a new Opportunity
        status = self.page.create_opportunity_for_existing_account(companyname=company + firstname_auto_code)
        if status == 0:
            print("Test:Attach Opportunity to Account - Pass ")
        else:
            print("Test:Attach Opportunity to Account - Fail ")

        print("XXXX END OF TEST XXXX")

        # Quit WebDriver
        self.driver_instance.quit_driver()

