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
        EC.element_to_be_clickable((By.XPATH, "//ion-item[@routerlink='/empleados']"))
    ).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ion-button[.//ion-icon[@name='close-outline']]"))
    ).click()

    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Registrar Empleado']"))
    ).click()
    time.sleep(3)
    #REGISTRO DEL NUEVO EMPLEADO
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='ci']"))
            ).send_keys("13760346")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='nombres']"))
            ).send_keys("Sergio")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='apellidos']"))
            ).send_keys("Poma")
    time.sleep(3)
    #Cargo
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ion-select[@name='id_cargo']"))
    ).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'alert-radio-button') and .//div[contains(text(), 'EMPLEADO')]]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'alert-button') and contains(., 'OK')]"))
    ).click()
    time.sleep(3)
    #---------------
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-item//ion-label[text()='Celular *']//following::input[@name='telefono']"))
            ).send_keys("69818390")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-item//ion-label[text()='Email Personal *']//following::input[@name='email']"))
            ).send_keys("sergiopoma@gmail.com")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-item//ion-label[text()='Dirección *']//following::input[@name='direccion']"))
            ).send_keys("Av Saavedra")
    time.sleep(3)
    #codigo para bajar el scroll del modal con TAB
    driver.find_element(By.XPATH, "//ion-item//ion-label[text()='Dirección *']//following::input[@name='direccion']").send_keys(Keys.TAB)

    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Agregar Empleado']"))
    ).click()
    time.sleep(3)

    print("CRUD EMPLEADOS222")
    driver.quit()  # FINNN



   
