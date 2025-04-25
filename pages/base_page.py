from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver


class BasePage:
    browser: ChromeWebDriver | FirefoxWebDriver

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
