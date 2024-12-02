import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from page_elements.admin_page.modulo_pagina_page import AdminPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #para el Tab

class TestCrearError:
    def test_uni(self):  # Agregar self como primer parámetro
        admin = AdminPage()
        driver = admin.ejecutar_login()
        print("CRUD EMPLEADOS")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-menu-button[contains(@class, 'buttons-men')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-item[@routerlink='/repuestos']"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-button[.//ion-icon[@name='close-outline']]"))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Registrar Repuesto']"))
        ).click()
        time.sleep(3)
        # REGISTRO DE REPUESTO
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='codigo_oem']"))
        ).send_keys("GTDRE0021")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='nombre']"))
        ).send_keys("Garra Mecanica Tractor")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='numero_serie']"))
        ).send_keys("Gt001124")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='descripcion']"))
        ).send_keys("Garra Mecanica para tractor")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='cantidad_stock']"))
        ).send_keys("10")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-select[@name='id_categoria']"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'alert-radio-button') and .//div[contains(text(), 'motor')]]"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='OK']]"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-select[@name='id_marca']"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'alert-radio-button') and .//div[contains(text(), 'caterpillar')]]"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='OK']]"))
        ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//ion-select[@name='id_marca']").send_keys(Keys.TAB)
        time.sleep(3)
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//ion-input[@name='costo_unitario']//input[@type='number']"))
        ).send_keys("2500")
        time.sleep(3)
        file_input = driver.find_element(By.XPATH, "//ion-item//input[@type='file']")
        time.sleep(3)
        file_input.send_keys("C:\\Users\\seros\\Downloads\\im1.jpg") 
        time.sleep(3)

        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Agregar Repuesto']"))
        ).click()
        time.sleep(3)

        print("CRUD EMPLEADOS222")
        driver.quit()  # FINNN
