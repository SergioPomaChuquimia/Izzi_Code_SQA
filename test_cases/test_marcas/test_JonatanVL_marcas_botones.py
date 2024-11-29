from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SolicitudGraficoTest:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/marcas')
        time.sleep(3)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_boton_eliminar(self):
        time.sleep(3)
        #esperado = ''
        self.driver.find_element(By.XPATH, "(//ion-button[@color = 'danger'])[2]").click()
        self.driver.find_element(By.XPATH, "//span[text() = 'Sí']").click()
        #actual

    def test_modal_actualizar(self):
        time.sleep(3)
        #esperado =
        self.driver.find_element(By.XPATH, "(//ion-button[@color = 'primary'])[1]").click()
