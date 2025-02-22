# pages/pg_base.py
from abc import ABC, abstractmethod
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def get_locators(self):
        """Abstract method to return locators. Must be implemented in subclass."""
        pass

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
