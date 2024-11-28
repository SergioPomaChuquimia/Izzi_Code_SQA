from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCrearCategoria:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/categorias')
        time.sleep(3)
    def teardown_method(self):
        self.driver.quit()
        print("prueba visual completada")

    def test_crearcategoria(self):
        esperado = "Categoria creada con éxito"
        self.driver.find_element(By.XPATH,"//ion-button[@color='success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").send_keys("categoria11")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='descripcion']").send_keys("descripcion 1")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Agregar Categoria']").click()
        time.sleep(6)
        actual = self.driver.find_element(By.XPATH,"//ion-text[@color='success']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"
        
    def test_editarcategoria(self):
        esperado = "Categoria actualizada con éxito"
        self.driver.find_element(By.XPATH,"//*[@id='main-content']//child::ion-item[4]//child::ion-button[@color='primary']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").send_keys("ncategoria")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='descripcion']").clear()
        time.sleep(2) 
        self.driver.find_element(By.XPATH,"//input[@name='descripcion']").send_keys("ndescripcion")
        time.sleep(2) 
        self.driver.find_element(By.XPATH,"//ion-button[text()='Actualizar Categoria']").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH,"//ion-text[@color='success']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"

    def test_eliminarcategoria(self):
        esperado = "Categoria eliminado con éxito"
        self.driver.find_element(By.XPATH,"//*[@id='main-content']//child::ion-item[4]//child::ion-button[@color='danger']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='alert-button ion-focusable ion-activatable sc-ion-alert-md']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH,"//ion-text[@color='success']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"

        





