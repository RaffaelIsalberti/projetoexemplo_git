import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

@pytest.mark.simu

class TestSimu():
    def test_simu_pytest_1(self):
        driver.get('https://www.saucedemo.com/v1/index.html')
        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        driver.find_element(By.ID, "password").send_keys('secret_sauce')
        driver.find_element(By.ID, "login-button").click()

    def test_simu_pytest_2(self):
        assert 1 == 1

