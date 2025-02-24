# utils/selenium_utils.py
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class SeleniumUtils:
    @staticmethod
    def wait_for_element(driver, locator, condition=EC.visibility_of_element_located, timeout=60):
        """
        Wait for an element to meet a certain condition (default: visibility).

        :param driver: WebDriver instance
        :param locator: Locator tuple (By, value)
        :param condition: The condition to wait for (default is visibility)
        :param timeout: The maximum time to wait for the condition (default is 10 seconds)
        :return: WebElement once the condition is met
        """
        return WebDriverWait(driver, timeout).until(condition(locator))

    @staticmethod
    def click(driver, locator):
        """
        Click on the element located by the given locator after waiting for the element to be clickable.
        """
        # Wait for element to be clickable
        element = SeleniumUtils.wait_for_element(driver, locator, EC.element_to_be_clickable)
        element.click()

    @staticmethod
    def enter_text(driver, locator, text):
        """
        Enter text into the field located by the given locator after waiting for the element to be visible.
        """
        # Wait for the element to be visible
        element = SeleniumUtils.wait_for_element(driver, locator, EC.visibility_of_element_located)
        element.send_keys(text)

    @staticmethod
    def navigate(driver, url):
        """
        Navigate to the given URL.
        """
        driver.get(url)

    @staticmethod
    def action_click(driver, locator):
        """
        Click on the element using ActionChains after waiting for it to be clickable.
        """
        # Wait for element to be clickable
        element = SeleniumUtils.wait_for_element(driver, locator, EC.element_to_be_clickable)
        action = ActionChains(driver)
        action.click(element).perform()

    @staticmethod
    def action_enter_text(driver, locator, text):
        """
        Enter text into the element using ActionChains after waiting for it to be visible.
        """
        # Wait for element to be visible
        element = SeleniumUtils.wait_for_element(driver, locator, EC.visibility_of_element_located)
        action = ActionChains(driver)
        action.click(element).send_keys(text).perform()

    @staticmethod
    def action_double_click(driver, locator):
        """
        Double-click on the element using ActionChains after waiting for it to be clickable.
        """
        # Wait for element to be clickable
        element = SeleniumUtils.wait_for_element(driver, locator, EC.element_to_be_clickable)
        action = ActionChains(driver)
        action.double_click(element).perform()

    @staticmethod
    def action_hover(driver, locator):
        """
        Hover over the element using ActionChains after waiting for it to be visible.
        """
        # Wait for element to be visible
        element = SeleniumUtils.wait_for_element(driver, locator, EC.visibility_of_element_located)
        action = ActionChains(driver)
        action.move_to_element(element).perform()

    @staticmethod
    def select_dropdown(driver, locator, option_text):
        """
        Select an option from a dropdown by visible text.
        """
        from selenium.webdriver.support.ui import Select
        select = Select(driver.find_element(*locator))
        select.select_by_visible_text(option_text)

    @staticmethod
    def get_page_title(driver):
        """
        Get the current page title.
        """
        return driver.title

    @staticmethod
    def wait_for_condition(driver, condition, timeout=30):
        """
        Wait for a specific condition to be met.

        :param driver: WebDriver instance
        :param condition: The condition to wait for (expected_conditions)
        :param timeout: The maximum time to wait for the condition (default is 30 seconds)
        """
        WebDriverWait(driver, timeout).until(condition)

    @staticmethod
    def generate_random_integer(start, end):
        """
        Generates a random integer between start and end (inclusive).

        :param start: The starting value of the range.
        :param end: The ending value of the range.
        :return: A random integer between start and end.
        """
        return randint(start, end)

    @staticmethod
    def send_enter(driver, locator):
        """
        Send the Enter key to an element after waiting for it to be visible.
        """
        # Wait for element to be visible
        element = SeleniumUtils.wait_for_element(driver, locator, EC.visibility_of_element_located)
        action = ActionChains(driver)
        action.click(element).send_keys(Keys.ENTER).perform()

    @staticmethod
    def get_attribute(driver, locator, attribute):
        """
        Get the value of a specified attribute for a given element after waiting for the element to be visible.

        :param driver: WebDriver instance
        :param locator: Locator tuple (By, value)
        :param attribute: The attribute name to retrieve (e.g., 'value', 'class', 'id', etc.)
        :return: The attribute value as a string.
        """
        # Wait for element to be visible
        element = SeleniumUtils.wait_for_element(driver, locator, EC.visibility_of_element_located)
        # Get the attribute value
        return element.get_attribute(attribute)

    @staticmethod
    def clear_text(driver, locator):
        """
        Clears the text from the input field located by the given locator.

        :param driver: WebDriver instance
        :param locator: Locator tuple (By, value)
        """
        # Wait for the element to be visible
        element = SeleniumUtils.wait_for_element(driver, locator, EC.visibility_of_element_located)
        # Clear the text from the element
        element.clear()
