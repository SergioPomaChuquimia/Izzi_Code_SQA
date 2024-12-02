from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestError:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/marcas')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("prueba visual completada")

    def test_crearmarcasnull(self):
        esperado1 = "El campo de nombre es obligatorio."
        esperado2 = "El país es obligatorio."
        self.driver.find_element(By.XPATH,"//ion-button[@color='success']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").send_keys(Keys.TAB)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Agregar Marca']").click()
        time.sleep(1)
        primer_campo =  self.driver.find_element(By.XPATH,"//ion-label[text()='Nombre *']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", primer_campo)
        time.sleep(1)
        actual1 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][1]").text
        actual2 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][2]").text

        assert (
            actual1 in esperado1 and
            actual2 in esperado2
        ), (
            f"El actual es: '{actual1}' y el esperado es: '{esperado1}', "
            f"El actual es: '{actual2}' y el esperado es: '{esperado2}', "
        )
        

    def test_crearMarcaRegex(self):
        esperado1 = "El nombre solo debe contener letras, números, puntos y espacios."
        esperado2 = "Introduzca un email valido"
        esperado3 = "La dirección solo debe contener letras y números."
        esperado4 = "Error con la url de sitio web."
        
        self.driver.find_element(By.XPATH,"//ion-button[@color='success']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").send_keys("#@$@5$#@")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//ion-select[@name='pais']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[text()=' Alemania ']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[@class='alert-button ion-focusable ion-activatable sc-ion-alert-md']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("#@$@5$#@")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='direccion']").send_keys("#@$@5$#@")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").send_keys("#@$@5$#@")
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").send_keys(Keys.TAB)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Agregar Marca']").click()
        time.sleep(4)

        primer_campo =  self.driver.find_element(By.XPATH,"//ion-label[text()='Nombre *']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", primer_campo)
        time.sleep(1)

        actual1 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][1]").text
        actual2 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][2]").text
        actual3 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][3]").text
        actual4 = self.driver.find_element(By.XPATH,"//div[@style='color: red; margin-bottom: 10px; text-align: center;'][4]").text

        assert (
            actual1 in esperado1 and
            actual2 in esperado2 and
            actual3 in esperado3 and 
            actual4 in esperado4
        ), (
            f"El actual es: '{actual1}' y el esperado es: '{esperado1}', "
            f"El actual es: '{actual2}' y el esperado es: '{esperado2}', "
            f"El actual es: '{actual3}' y el esperado es: '{esperado3}', "
            f"El actual es: '{actual4}' y el esperado es: '{esperado4}', "
        )


      

