import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_pages import LoginPage


# from selenium import webdriver
@pytest.mark.usefixtures("setup_teardown")
class Testct01comp:
    def test_ct01_comp(self):
        driver = conftest.driver
        login_pages = LoginPage()

        #fazer login
        login_pages.fazer_login ("standard_user","secret_sauce")
        # driver.find_element(By.ID, "user-name").send_keys('standard_user')
        # driver.find_element(By.ID, "password").send_keys('secret_sauce')
        # driver.find_element(By.ID, "login-button").click()

        #realizar compra
        driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text() ='Sauce Labs Backpack' ]").click()
        driver.find_element(By.XPATH, "//button[@class='btn_primary btn_inventory']").click()
        driver.find_element(By.XPATH, "//button[@class='inventory_details_back_button']").click()
        driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text() ='Sauce Labs Bike Light' ]").click()
        driver.find_element(By.XPATH, "//button[@class='btn_primary btn_inventory']").click()
        driver.find_element(By.XPATH, "//*[@data-icon='shopping-cart']").click()

        #finalizar compra
        driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']").click()
        driver.find_element(By.ID, "first-name").send_keys('QEQWEQW')
        driver.find_element(By.ID, "last-name").send_keys('SADASDSAD')
        driver.find_element(By.ID, "postal-code").send_keys('12165165')
        driver.find_element(By.XPATH, "//input[@class='btn_primary cart_button']").click()
        driver.find_element(By.XPATH, "//a[@class='btn_action cart_button']").click()

        assert driver.find_element(By.XPATH, "//h2[@class='complete-header' and text() = 'THANK YOU FOR YOUR ORDER']")

        driver.close()

@pytest.mark.usefixtures("setup_teardown")
class Testct02comp:
    def test_ct02_comp(self):
        driver = conftest.driver
        #fazer login
        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        driver.find_element(By.ID, "password").send_keys('secret_sauce')
        driver.find_element(By.ID, "login-button").click()

        #realizar compra
        driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text() ='Sauce Labs Backpack' ]").click()
        driver.find_element(By.XPATH, "//button[@class='btn_primary btn_inventory']").click()
        driver.find_element(By.XPATH, "//button[@class='inventory_details_back_button']").click()
        driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text() ='Sauce Labs Bike Light' ]").click()
        driver.find_element(By.XPATH, "//button[@class='btn_primary btn_inventory']").click()
        driver.find_element(By.XPATH, "//*[@data-icon='shopping-cart']").click()

        #finalizar compra
        driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']").click()
        driver.find_element(By.ID, "first-name").send_keys('QEEQ QEQEQE')
        driver.find_element(By.ID, "last-name").send_keys('CVWVEWF')
        driver.find_element(By.ID, "postal-code").send_keys('8419151')
        driver.find_element(By.XPATH, "//input[@class='btn_primary cart_button']").click()
        driver.find_element(By.XPATH, "//a[@class='btn_action cart_button']").click()

        assert driver.find_element(By.XPATH, "//h2[@class='complete-header' and text() = 'THANK YOU FOR YOUR ORDER']")

        driver.close()

