from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestIniciarSesion:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/login')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("prueba visual completada")
        
    def test_iniciarSesion(self):
        esperado = "Usuario: cca757266"
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("cca757266")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("141308")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Iniciar Sesión']").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH,"//h6[@class='email-text']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"

    def test_iniciarSesionnull(self):
        esperado1 = "El campo de codigo es obligatorio."
        esperado2 = "El campo de contraseña es obligatorio."
        self.driver.find_element(By.XPATH,"//ion-button[text()='Iniciar Sesión']").click()
        time.sleep(2)
        actual1 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][1]").text
        time.sleep(1)
        actual2 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][2]").text
        assert actual1 == esperado1 and actual2 == esperado2, f"El actual es: '{actual1}' y el esperado es: '{esperado1}', o el actual es: '{actual2}' y el esperado es: '{esperado2}'"

    def test_iniciarSesioncreden_invalidas(self):
        esperado = "Credenciales inválidas"
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("cca757412")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("141708")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Iniciar Sesión']").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH,"//div[@style='color: red;']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"

    #def test_ingresarcategorias(self):
        #esperado =""
        #self.driver.find_element(By.XPATH,"//ion-menu-button[@class='buttons-men sc-ion-buttons-md md button in-toolbar ion-activatable ion-focusable hydrated']").click()