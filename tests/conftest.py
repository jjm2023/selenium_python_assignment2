import pytest
from utils.webdrivermanager import WebDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Fixture to initialize the WebDriver and ensure cleanup.
    """
    driver_manager = WebDriverManager(browser="chrome", headless=False)  # Change headless to True if you need headless
    driver = driver_manager.get_driver()

    # Yield the driver to the test function
    yield driver

    # Quit the WebDriver after the test
    driver_manager.quit_driver()
