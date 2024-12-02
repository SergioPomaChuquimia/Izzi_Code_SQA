from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestCrearMarca:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/marcas')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("prueba visual completada")
        
    def test_crearMarca(self):
        esperado = "Marca creada con éxito"

        self.driver.find_element(By.XPATH,"//ion-button[@color='success']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").send_keys("marca777")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//ion-select[@name='pais']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//div[text()=' Alemania ']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@class='alert-button ion-focusable ion-activatable sc-ion-alert-md']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("dsfa@gmail.com")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='direccion']").send_keys("av 123 zona 14")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").send_keys("http://localhost:8100/marcas")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").send_keys(Keys.TAB)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='descripcion']").send_keys("descripcion de prueba automatizada")
        self.driver.find_element(By.XPATH,"//ion-button[text()='Agregar Marca']").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH,"//ion-text[@color='success']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"
        
    def test_editarMarca(self):
        esperado = "Marca actualizada con éxito"
        self.driver.find_element(By.XPATH,"//*[@id='main-content']//child::ion-item[3]//child::ion-button[@color='primary']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,"//input[@name='nombre']").clear()
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").send_keys("nueva marca777")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//ion-select[@name='pais']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//div[text()=' Brasil ']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@class='alert-button ion-focusable ion-activatable sc-ion-alert-md']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='email']").clear()
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("nuevodsfa@gmail.com")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='direccion']").clear()
        self.driver.find_element(By.XPATH,"//input[@name='direccion']").send_keys("nueva av 123 zona 14")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").clear()
        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").send_keys("http://localhost:8100/nuevasmarcas")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='sitio_web']").send_keys(Keys.TAB)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='descripcion']").clear()
        self.driver.find_element(By.XPATH,"//input[@name='descripcion']").send_keys("nueva descripcion de prueba automatizada")

        self.driver.find_element(By.XPATH,"//ion-button[text()='Actualizar Marca']").click()
        time.sleep(5)


        actual = self.driver.find_element(By.XPATH,"//ion-text[@color='success']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"

    def test_eliminarcategoria(self):
        esperado = "Marca eliminado con éxito"
        self.driver.find_element(By.XPATH,"//*[@id='main-content']//child::ion-item[3]//child::ion-button[@color='danger']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='alert-button ion-focusable ion-activatable sc-ion-alert-md']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH,"//ion-text[@color='success']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"


        




    

