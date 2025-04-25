import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language",
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Headless mode: true or false",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    headless = request.config.getoption("headless") == "true"

    print(f"\nSelected browser: {browser_name}\nLanguage: {user_language}")

    browser = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        if headless:
            options.add_argument("--headless=new")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        fp = webdriver.FirefoxOptions()
        fp.set_preference("intl.accept_languages", user_language)
        if headless:
            fp.add_argument("--headless")
        browser = webdriver.Firefox(options=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()
