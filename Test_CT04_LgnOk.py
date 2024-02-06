import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_pages import LoginPage


@pytest.mark.usefixtures("setup_teardown2")
class Testct04Lgn:
    def test_ct04_login(self):
        driver = conftest.driver
        login_pages = LoginPage()
        # fazer login
        login_pages.fazer_login1("isalberti@hotmail.com", "R@affialh1")
        # driver.find_element(By.XPATH, "//input[@name='username']").send_keys('isalberti@hotmail.com')
        # driver.find_element(By.XPATH, "//input[@name='password']").send_keys('R@affialh1')
        # driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert driver.find_element(By.XPATH, "//input[@name='verificationCode']")
