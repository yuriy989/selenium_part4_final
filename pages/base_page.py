from math import log, sin

from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    browser: ChromeWebDriver | FirefoxWebDriver
    timeout: int

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)
        self.url = url

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        self.browser.implicitly_wait(0)
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        finally:
            self.browser.implicitly_wait(self.timeout)

        return False

    def is_disappeared(self, how, what, timeout=4):
        self.browser.implicitly_wait(0)
        try:
            WebDriverWait(
                self.browser,
                timeout,
                poll_frequency=1,
                ignored_exceptions=[TimeoutException],
            ).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        finally:
            self.browser.implicitly_wait(self.timeout)

        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), (
            "Login link is not presented"
        )

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
