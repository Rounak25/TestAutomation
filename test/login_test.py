from selenium import webdriver
import pytest
import allure
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import utils as utils
import moment


@pytest.mark.usefixtures("test_setup")
class Test_Login():

    def test_login(self):
        driver = self.driver
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

    def test_logout(self):
        try:
            driver = self.driver
            logout = HomePage(driver)
            logout.click_Welcome()
            logout.click_Logout()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("There is an error")
            print(error)
            currTime= moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName_ScreenshotName = utils.whomami()
            screenshotname = testName_ScreenshotName + "__" + "ScreenshotName"+ "_" +currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotname,
                          attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("Exception is handling here")

        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()

    #(In above, we have used "assert" statement, therfore Assertion Error we are catching
    # #Other than "Assertion" any error occur we can catch in except block )

