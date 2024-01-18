import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)
driver.get('https://www.monteleste.com.br/')

time.sleep(2)
driver.find_element(By.XPATH, '//div/div/div/div[@class="swiper-button-next"][1]').click()
driver.find_element(By.XPATH, '//*[@src="https://global.cdn.magazord.com.br/monteleste/img/2023/10/banner/1913/bermudas-lisas-banner.png"]').click()
# BERMUDA ROSA
driver.find_element(By.XPATH, '//a[@href="/shorts-bermuda-d-agua-elastic-misiones"]').click()
driver.find_element(By.XPATH, '//*[contains(text(), "GG")]').click()
driver.find_element(By.XPATH, '//div[@class="area-compra-btn"]').click()
driver.find_element(By.XPATH, '//button[@class="swal2-confirm botao-continuar-comprando swal2-styled swal2-default-outline"]').click()
# BERMUDA BRANCA
driver.find_element(By.XPATH, '//a[@href="/shorts/shorts-bermuda-d-agua-monte-leste-branco--p"]').click()
driver.find_element(By.XPATH, '//*[contains(text(), "GG")]').click()
driver.find_element(By.XPATH, '//div[@class="area-compra-btn"]').click()
driver.find_element(By.XPATH, '//button[@class="swal2-confirm botao-continuar-comprando swal2-styled swal2-default-outline"]').click()

# BERMUDA PRETO
driver.find_element(By.XPATH, '//a[@href="/shorts/shorts-bermuda-d-agua-monte-leste-preto--p"]').click()
driver.find_element(By.XPATH, '//*[contains(text(), "GG")]').click()
driver.find_element(By.XPATH, '//div[@class="area-compra-btn"]').click()
driver.find_element(By.XPATH, '//button[@class="swal2-deny botao-finalizar-compra swal2-styled swal2-default-outline"]').click()
driver.find_element(By.XPATH, '//img[@src="https://global.cdn.magazord.com.br/monteleste/img/2022/10/produto/1051/2.png"]').click()
driver.find_element(By.XPATH, '//input[@class="input-cep"]').send_keys('38408698')
# driver.find_element(By.XPATH, '//button[@onclick="Zord.Cart.atualizaValorTotalPedidoCarrinho();"]').send_keys('38408698')

time.sleep(2)
