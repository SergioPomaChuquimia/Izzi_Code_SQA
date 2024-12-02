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
        self.driver.find_element(By.XPATH, "//ion-button[@color = 'success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//ion-button[@type = 'submit']").click()
        time.sleep(2)
        actual1 = self.driver.find_element(By.XPATH, "//div[text() = ' El campo de nombre es obligatorio. ']").text
        actual2 = self.driver.find_element(By.XPATH, "//div[text() = ' El país es obligatorio. ']").text
        assert esperado1 == actual1 and esperado2 == actual2

    def test_registro(self):
        time.sleep(3)
        esperado = ''
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
