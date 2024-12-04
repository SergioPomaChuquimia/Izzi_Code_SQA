from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestMarcasGeneral:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/marcas')
        time.sleep(5)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_msg_validaciones(self):
        time.sleep(3)
        esperado1 = " El campo de nombre es obligatorio. "
        esperado2 = " El país es obligatorio. "
        esperado3 = " Introduzca un email valido "
        esperado4 = " La dirección solo debe contener letras y números. "
        esperado5 = " Error con la url de sitio web. "
        self.driver.find_element(By.XPATH, "//ion-button[@color = 'success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//ion-input[@name='email'])[2]").send_keys('a')
        self.driver.find_element(By.XPATH, "(//ion-input[@name='direccion']").send_keys('$@#')
        self.driver.find_element(By.XPATH, "(//ion-input[@name='sitio_web']").send_keys('a')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//ion-button[@type = 'submit']").click()
        actual1 = self.driver.find_element(By.XPATH, "//div[text() = ' El campo de nombre es obligatorio. ']").text
        actual2 = self.driver.find_element(By.XPATH, "//div[text() = ' El país es obligatorio. ']").text
        actual3 = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Intro')]").text
        actual4 = self.driver.find_element(By.XPATH, "//div[contains(text(), 'La')]").text
        actual5 = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Error')]").text
        assert esperado1 == actual1 and esperado2 == actual2 and actual3 == esperado3 and actual4 == esperado4 and actual5 == esperado5

    def test_registro(self):
        time.sleep(3)
        esperado = ' Marca creada con éxito '
        self.driver.find_element(By.XPATH, "//ion-button[@color = 'success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id = 'ion-input-0']").send_keys("testClase")
        self.driver.find_element(By.XPATH, "//ion-select[@name = 'pais']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text() = ' Bolivia ']").click()
        self.driver.find_element(By.XPATH, "//ion-button[@type = 'submit']").click()
        time.sleep(3)
        actual = self.driver.find_element(By.XPATH, "//ion-text[@color = 'success']").text
        assert actual == esperado
