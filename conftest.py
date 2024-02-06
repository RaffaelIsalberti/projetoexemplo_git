import pytest
from selenium import webdriver

driver: webdriver.remote


@pytest.fixture
def setup_teardown():
    #setup
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.saucedemo.com/v1/index.html')

    #run test
    yield

    #teardown
    driver.quit()

@pytest.fixture
def setup_teardown2():
    #setup
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.instagram.com/')

    #run test
    yield

    #teardown
    driver.quit()
