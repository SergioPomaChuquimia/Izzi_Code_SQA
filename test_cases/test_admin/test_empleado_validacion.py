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
    #REGISTRO DEL NUEVO EMPLEADO-----------------------------------------------------------------
    #codigo para bajar el scroll del modal con TAB
    driver.find_element(By.XPATH, "//ion-item//ion-label[text()='Dirección *']//following::input[@name='direccion']").send_keys(Keys.TAB)
    time.sleep(3)
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Agregar Empleado']"))
    ).click()
    time.sleep(3)
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'La dirección es obligatoria.')]"))
    )
    actual = driver.find_element(By.XPATH, "//div[contains(text(), 'La dirección es obligatoria.')]").text
    print("++++++++", actual)
    esperado = "La dirección es obligatoria."
    assert actual == esperado, f"Error: se esperaba '{esperado}', pero se obtuvo '{actual}'"
    
    print("CRUD EMPLEADOS222")
    driver.quit()  # FINNN



   
