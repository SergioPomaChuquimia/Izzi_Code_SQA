from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCrearError:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8100/categorias')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("prueba visual completada")
        
    def test_crearcategorianull(self):
        esperado = "El campo de nombre es obligatorio."
        self.driver.find_element(By.XPATH,"//ion-button[@color='success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Agregar Categoria']").click()
        time.sleep(6)
        actual = self.driver.find_element(By.XPATH,"//div[text()=' El campo de nombre es obligatorio. ']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"
    
    def test_crearcategoriaregex(self):
        esperado = "El nombre solo debe contener letras, números, espacios y puntos."
        self.driver.find_element(By.XPATH,"//ion-button[@color='success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").send_keys("#@$@5$#@")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Agregar Categoria']").click()
        time.sleep(6)
        actual = self.driver.find_element(By.XPATH,"//div[text()=' El nombre solo debe contener letras, números, espacios y puntos. ']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"

    def test_crearcategoria(self):
        esperado = "Solo se permite hasta maximo 30 caracteres en el campo nombre."
        self.driver.find_element(By.XPATH,"//ion-button[@color='success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombre']").send_keys("dghasdkfjdsjgdsajfdsjfdsjflkdsjkdsjgldsjfdsnfljdsaf")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ion-button[text()='Agregar Categoria']").click()
        time.sleep(6)
        actual = self.driver.find_element(By.XPATH,"//div[text()=' Solo se permite hasta maximo 30 caracteres en el campo nombre. ']").text
        assert actual in esperado, f"El actual es:{actual} y el esperado es:{esperado}"

