from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in which browser Chrome or Firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/cp/PycharmProjects/EntireTask/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:/Users/cp/PycharmProjects/EntireTask/drivers/geckodriver.exe")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Done")