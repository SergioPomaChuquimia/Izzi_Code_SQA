from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSolicitudGrafico:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/solicitud-grafico')
        time.sleep(5)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_correct(self):
        time.sleep(3)
        esperado1 = 'Se recomienda comprar este producto.'
        esperado2 = 'No se recomienda comprar este producto.'
        self.driver.find_element(By.XPATH, "//input[@id= 'ion-input-2']").send_keys("6")
        self.driver.find_element(By.XPATH, "//ion-select").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@id = 'alert-input-2-24']").click()
        self.driver.find_element(By.XPATH, "//ion-button[text() = 'Enviar']").click()
        actual = self.driver.find_element(By.XPATH, "//ion-note[@color = 'danger']").text
        self.print('+++++++++++++++')
        time.sleep(8)
        assert actual == esperado1 or actual == esperado2
