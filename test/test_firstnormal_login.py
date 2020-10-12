from selenium import webdriver
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import utils as utils

# It uses homepage, utils, loginpage action.

class Test_Login():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/cp/PycharmProjects/EntireTask/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Done")

    def test_login(self,test_setup):
        #driver.get("https://opensource-demo.orangehrmlive.com")
        driver.get(utils.URL)
        login = LoginPage(driver)
        #login.enter_username("Admin")
        login.enter_username(utils.USERNAME)
        #login.enter_password("admin123")
        login.enter_password(utils.PASSWORD)
        login.clickonLogin()

        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()

    def test_logout(self,test_setup):
        logout = HomePage(driver)
        logout.click_Welcome()
        logout.click_Logout()

        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()


