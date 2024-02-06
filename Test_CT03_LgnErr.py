import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_pages import LoginPage


# from selenium import webdriver
@pytest.mark.usefixtures("setup_teardown")
class Testct03Lgn:
    def test_ct03_login(self):
        driver = conftest.driver
        login_pages = LoginPage()

        # fazer login
        login_pages.fazer_login('standard_user','senha_incorrect')
        # driver.find_element(By.ID, "user-name").send_keys('standard_user')
        # driver.find_element(By.ID, "password").send_keys('senh_incorret')
        # driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "//button[@class='error-button']")
