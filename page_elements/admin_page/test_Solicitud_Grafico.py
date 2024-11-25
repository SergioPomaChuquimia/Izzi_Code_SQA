from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SolicitudGraficoTest:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/solicitud-grafico')
        time.sleep(5)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def Test_Correct(self):
        time.sleep(3)
        esperado = 'Datos procesados e insertados correctamente.'
        self.driver.find_element(By.XPATH, "//input[@id= 'ion-input-2']").send_keys("6")
        self.driver.find_element(By.XPATH, "//ion-select").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@id = 'alert-input-2-24']").click()
        self.driver.find_element(By.XPATH, "//ion-button[text() = 'Enviar']").click()
        actual = self.driver.find_element(By.XPATH, "//ion-note[@color = 'danger']").text
        self.print('+++++++++++++++')
        assert actual == esperado
