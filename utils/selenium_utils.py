# utils/selenium_utils.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumUtils:
    @staticmethod
    def click(driver, locator):
        """
        Click on the element located by the given locator.
        """
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    @staticmethod
    def enter_text(driver, locator, text):
        """
        Enter text into the field located by the given locator.
        """
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    @staticmethod
    def navigate(driver, url):
        """
        Navigate to the given URL.
        """
        driver.get(url)

    @staticmethod
    def action_click(driver, element):
        """
        Click on the element using ActionChains (useful for complex elements).
        """
        action = ActionChains(driver)
        action.click(element).perform()

    @staticmethod
    def action_enter_text(driver, element, text):
        """
        Enter text into the element using ActionChains (useful for complex inputs).
        """
        action = ActionChains(driver)
        action.click(element).send_keys(text).perform()

    @staticmethod
    def action_double_click(driver, element):
        """
        Double-click an element using ActionChains.
        """
        action = ActionChains(driver)
        action.double_click(element).perform()

    @staticmethod
    def action_hover(driver, element):
        """
        Hover over an element using ActionChains.
        """
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
