# utils/conftest.py
import pytest
from utils.wedriver_manager import WebDriverManager

@pytest.fixture()
def driver():
    # Initialize the WebDriverManager
    webdriver_manager = WebDriverManager(browser="chrome", headless=False)

    # Get the WebDriver instance
    driver = webdriver_manager.get_driver()

    # Yield the driver to the tests
    yield driver

    # Cleanup after the test
    webdriver_manager.quit_driver()
