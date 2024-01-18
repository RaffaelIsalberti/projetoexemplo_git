import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.saucedemo.com/v1/index.html')
driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.ID, "password").send_keys('secret_sauc')
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, "//*[@data-icon='times-circle']").is_displayed()
