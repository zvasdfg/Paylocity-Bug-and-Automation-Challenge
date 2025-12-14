import allure
import time
from src.core.driver_factory import DriverFactory
from src.pages.login_page import LoginPage

@allure.feature("Login")
def test_valid_login():
    driver = DriverFactory.create_driver()
    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")

    login = LoginPage(driver)
    login.login("TestUser845", "KQ.]SfeU>OYI")

    assert "Dashboard" in driver.title
    time.sleep(5)
    ##driver.quit()
