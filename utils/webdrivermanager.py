from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebDriverManager:
    def __init__(self, browser="chrome", headless=False):
        self.browser = browser
        self.headless = headless
        self.driver = None

    def get_driver(self):
        """
        Initialize the WebDriver (currently supports Chrome).
        """
        if self.browser.lower() == "chrome":
            chrome_options = Options()

            # Optional: Disable notifications
            chrome_options.add_argument("--disable-notifications")

            # Headless mode configuration (optional)
            if self.headless:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")  # For headless mode

            # Set the path to Chrome binary if not in the PATH (optional)
            chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

            # Initialize the Chrome WebDriver
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )

            # Maximize the browser window
            self.driver.maximize_window()

        # You can later add more browsers, like Firefox or Edge, if needed.
        return self.driver

    def quit_driver(self):
        """
        Quits the WebDriver session.
        """
        if self.driver:
            self.driver.quit()
            self.driver = None  # Ensure to clear the driver reference
