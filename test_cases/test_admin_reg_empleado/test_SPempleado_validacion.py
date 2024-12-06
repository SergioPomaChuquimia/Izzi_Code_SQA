import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_elements.admin_page.modulo_login_page import AdminPage
from selenium.webdriver.common.keys import Keys #para el Tab

class TestEmplado:
    def setup_method(self, driver):

        admin = AdminPage()
        self.driver = admin.ejecutar_login()
        print("CRUD EMPLEADOS")
        time.sleep(3)

    def teardown_method(self):

        print("Fin de prueba CRUD EMPLEADOS")
        self.driver.quit()

    def test_valiacion_empleados(self):
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
        #REGISTRO DEL NUEVO EMPLEADO-----------------------------------------------------------------
        self.driver.find_element(By.XPATH, "//ion-item//ion-label[text()='Dirección *']//following::input[@name='direccion']").send_keys(Keys.TAB)
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Agregar Empleado']"))
        ).click()
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            #EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'La dirección es obligatoria.')]"))
            EC.visibility_of_element_located((By.XPATH, "(//div[@style='color: red; margin-bottom: 10px; text-align: center;'])[7]"))
        )
        #actual = self.driver.find_element(By.XPATH, "//div[contains(text(), 'La dirección es obligatoria.')]").text
        actual = self.driver.find_element(By.XPATH, "(//div[@style='color: red; margin-bottom: 10px; text-align: center;'])[7]").text
        print("++++++++", actual)
        
        esperado = "La dirección es obligatoria."
        assert actual == esperado, f"Error: se esperaba '{esperado}', pero se obtuvo '{actual}'"
        
        print("CRUD EMPLEADOS222")
        self.driver.quit()  # FINNN



   
