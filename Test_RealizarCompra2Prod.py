import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.saucedemo.com/v1/index.html')
driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.ID, "password").send_keys('secret_sauce')
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text() ='Sauce Labs Backpack' ]").click()
driver.find_element(By.XPATH, "//button[@class='btn_primary btn_inventory']").click()
driver.find_element(By.XPATH, "//button[@class='inventory_details_back_button']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text() ='Sauce Labs Bike Light' ]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='btn_primary btn_inventory']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@data-icon='shopping-cart']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']").click()
time.sleep(1)
driver.find_element(By.ID, "first-name").send_keys('Raffael')
time.sleep(1)
driver.find_element(By.ID, "last-name").send_keys('Isalberti')
time.sleep(1)
driver.find_element(By.ID, "postal-code").send_keys('38408698')
time.sleep(1)
driver.find_element(By.XPATH, "//input[@class='btn_primary cart_button']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@class='btn_action cart_button']").click()

assert driver.find_element(By.XPATH, "//h2[@class='complete-header' and text() = 'THANK YOU FOR YOUR ORDER']")
time.sleep(2)
driver.close()


