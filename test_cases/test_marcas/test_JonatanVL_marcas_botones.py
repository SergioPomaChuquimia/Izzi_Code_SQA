from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestBotonesMarcas:
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
        esperado = ' Marca eliminado con éxito '
        self.driver.find_element(By.XPATH, "(//ion-button[@color = 'danger'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text() = 'Sí']").click()
        actual = self.driver.find_element(By.XPATH, "//ion-text[@color = 'success']").text
        
        assert actual == esperado

    def test_modal_actualizar(self):
        time.sleep(3)
        esperado = ' Marca actualizada con éxito '
        self.driver.find_element(By.XPATH, "(//ion-button[@color = 'primary'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='ion-input-2']").send_keys(f'{esperado}')
        boton_registro = self.driver.find_element(By.XPATH, "(//ion-button[@type='submit'])[2]")
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", boton_registro)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//ion-button[@type='submit'])[2]").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//ion-text[@color = 'success']").text
        assert actual == esperado
