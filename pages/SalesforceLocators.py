from selenium.webdriver.common.by import By


class SalesforceLocators:

    """Login Page"""
    TXT_USERNAME = (By.XPATH, "//input[@id='username' and @type='email']")
    TXT_PASSWORD = (By.XPATH, "//input[@id='password' and @type='password']")
    BTN_LOGIN = (By.XPATH, "//input[@id='Login' and @type='submit']")

    """Sales Landing Page"""
    SPN_SALES = (By.XPATH, "//span[contains(@class, 'app') and contains(text(), 'Sales')]")
    LNK_LEADS_HOME = (By.XPATH, "//a[@title='Leads']")
    LNK_CONTACT_HOME = (By.XPATH, "//a[@title='Contacts']")
    LNK_ACCOUNTS_HOME = (By.XPATH, "//a[@title='Accounts']")
    LNK_OPPORTUNITIES_HOME = (By.XPATH, "//a[@title='Opportunities']")
    DRP_LEADS = (By.XPATH, "//a[contains(@title, 'Leads')]/following::one-app-nav-bar-item-dropdown[1]")
    DRP_CONTACTS = (By.XPATH, "//a[contains(@title, 'Contacts')]/following::one-app-nav-bar-item-dropdown[1]")
    DRP_ACCOUNTS = (By.XPATH, "//a[contains(@title, 'Accounts')]/following::one-app-nav-bar-item-dropdown[1]")
    DRP_OPPORTUNITIES = (By.XPATH, "//a[contains(@title, 'Opportunities')]/following::one-app-nav-bar-item-dropdown[1]")
    LNK_NEW_LEAD = (By.XPATH,"//span[text()='New Lead']")
    LNK_NEW_CONTACT = (By.XPATH, "//span[text()='New Contact']")
    LNK_NEW_ACCOUNT = (By.XPATH, "//span[text()='New Account']")
    LNK_NEW_OPPORTUNITY = (By.XPATH, "//span[text()='New Opportunity']")

    """Leads Form"""
    TXT_SALUTATION = (By.XPATH, "//button[contains(@id, 'combobox') and contains(@aria-label,'Salutation')]")
    TXT_FIRST_NAME = (By.XPATH, "//input[contains(@placeholder, 'First Name')]")
    TXT_LAST_NAME = (By.XPATH, "//input[contains(@placeholder, 'Last Name')]")
    TXT_COMPANY = (By.XPATH, "//input[contains(@name ,'Company')]")
    BTN_SAVE = (By.XPATH, "//button[text()='Save']")

    """Leads Landing Page"""
    TXT_SEARCH_ITEM = (By.XPATH, "//input[@type='search' and contains(@aria-label, 'Search this list')]")
    TXT_LEAD_NAME = (By.XPATH, "//a[@data-refid='recordId'][1]")
    TXT_ACCOUNT_NAME = (By.XPATH, "(//a[@data-refid='recordId'])[1]")
    BTN_CONVERT_LEAD = (By.XPATH, "//button[text()='Convert']")

    """Convert Leads Form"""
    BTN_DISMISS = (By.XPATH, "//button[text()='Dismiss']")
    BTN_SUBMIT_FORM_1 = (By.XPATH, "//div[contains(@class, 'modal-footer')]//span//button")
    BTN_SUBMIT_FORM_2 = (By.XPATH, "//div[contains(@class, 'modal-footer')]//button[2]")
    MSG_CONVERT_SUCCESS = (By.XPATH, "//h2[text()='Your lead has been converted']")

    """Accounts Landing Page"""
    BTN_NEW_CONTACT_FOR_ACCOUNT = (By.XPATH, "//button[text()='New Contact']")
    BTN_NEW_OPPORTUNITY_FOR_ACCOUNT = (By.XPATH, "//button[text()='New Opportunity']")

    """Create Contact Form"""
    BTN_SAVE_NEW_CONTACT = (By.XPATH, "//footer//button//span[text()='Save']")
    TXT_COMPANY_NAME = (By.XPATH, "(//a[@data-refid='recordId'])[2]")

    """Create Opportunity Form"""
    TXT_OPPORTUNITY_NAME = (By.XPATH, "//span[text()='Opportunity Name']/following::input[@type='text'][1]")
    BTN_SAVE_NEW_OPPORTUNITY = (By.XPATH, "//footer//button//span[text()='Save']")