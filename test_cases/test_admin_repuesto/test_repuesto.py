import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from page_elements.admin_page.modulo_pagina_page import AdminPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #para el Tab

def test_uni():
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
    #REGISTRO DE REPUESTO
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='codigo_oem']"))
            ).send_keys("GT003BD")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='nombre']"))
            ).send_keys("GT003BD")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='numero_serie']"))
            ).send_keys("GT003BD")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='descripcion']"))
            ).send_keys("GT003BD")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='cantidad_stock']"))
            ).send_keys("GT003BD")
    time.sleep(3)

    print("CRUD EMPLEADOS222")
    driver.quit()  # FINNN