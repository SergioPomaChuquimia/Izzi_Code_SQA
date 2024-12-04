import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_elements.admin_page.modulo_login_page import AdminPage
from selenium.webdriver.common.keys import Keys  # Para el Tab

class TestEmplado:
    def setup_method(self, driver):
        admin = AdminPage()
        self.driver = admin.ejecutar_login()
        print("CRUD EMPLEADOS")
        time.sleep(3)

    def teardown_method(self):
        print("Fin de prueba CRUD EMPLEADOS")
        self.driver.quit()

    def test_abrir_empleados(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-menu-button[contains(@class, 'buttons-men')]"))
        ).click()
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-item[@routerlink='/empleados']"))
        ).click()
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-button[.//ion-icon[@name='close-outline']]"))
        ).click()
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Registrar Empleado']"))
        ).click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='ci']"))
        ).send_keys("13760346")
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='nombres']"))
        ).send_keys("Sergio")
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='apellidos']"))
        ).send_keys("Poma")
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-select[@name='id_cargo']"))
        ).click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'alert-radio-button') and .//div[contains(text(), 'EMPLEADO')]]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'alert-button') and contains(., 'OK')]"))
        ).click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-item//ion-label[text()='Celular *']//following::input[@name='telefono']"))
        ).send_keys("69818390")
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-item//ion-label[text()='Email Personal *']//following::input[@name='email']"))
        ).send_keys("sergiopoma@gmail.com")
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-item//ion-label[text()='Dirección *']//following::input[@name='direccion']"))
        ).send_keys("Av Saavedra")
        time.sleep(3)

        # Bajar el scroll del modal con TAB
        self.driver.find_element(By.XPATH, "//ion-item//ion-label[text()='Dirección *']//following::input[@name='direccion']").send_keys(Keys.TAB)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Agregar Empleado']"))
        ).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ion-text[@color='success' and contains(text(), 'Empleado creado con éxito')]"))
        )

        actual = self.driver.find_element(By.XPATH, "//ion-text[@color='success' and contains(text(), 'Empleado creado con éxito')]").text
        print("++++++++", actual)

        esperado = "Empleado creado con éxito"

        assert actual == esperado, f"Error: se esperaba '{esperado}', pero se obtuvo '{actual}'"

        
