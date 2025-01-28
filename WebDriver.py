from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebDriver:
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        """
        Initialize the Chrome WebDriver using the WebDriverManager.
        """
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")  # Disable pop-up notifications

        # Set the path to your Chrome executable (optional, only if not in PATH)
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        # Maximize the browser window
        self.driver.maximize_window()

        return self.driver

    def quit_driver(self):
        """
        Quits the WebDriver session.
        """
        if self.driver:
            self.driver.quit()
