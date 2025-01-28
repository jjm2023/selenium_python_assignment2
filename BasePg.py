from abc import abstractmethod

"""Inherited by all page classes"""

class BasePg:
    def __init__(self, driver):
        self.driver = driver  # WebDriver passed from WebDriver class

    def get_driver(self):
        """
        Returns the WebDriver instance.
        """
        return self.driver

    @abstractmethod
    def get_locator(self):
        """Abstract method to return locators. Must be implemented in subclass."""
        pass
