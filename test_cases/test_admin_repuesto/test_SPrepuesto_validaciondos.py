import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_elements.admin_page.modulo_login_page import AdminPage


class TestValidacionRepuestoObligatorios:
    def setup_method(self):
        admin = AdminPage()
        self.driver = admin.ejecutar_login()
        print("Iniciando pruebas de validación de campos obligatorios en el módulo de repuestos")
        time.sleep(3)

    def teardown_method(self):
        print("Pruebas de validación completadas")
        self.driver.quit()

    def test_val_obligatorios(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-menu-button[contains(@class, 'buttons-men')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-item[@routerlink='/repuestos']"))
        ).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-button[.//ion-icon[@name='close-outline']]"))
        ).click()
        time.sleep(3)
        

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-button[text()='Registrar Repuesto']"))
        ).click()
        time.sleep(3)

        esperado1 = "El código OEM es obligatorio."
        esperado2 = "El campo de nombre es obligatorio."
        esperado3 = "El número de serie es obligatorio."
        esperado4 = "El campo de categoría es obligatorio."
        esperado5 = "El campo de marca es obligatorio."
        
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_stock']").send_keys(Keys.TAB)
        time.sleep(3)
        
        self.driver.find_element(By.XPATH, "//ion-select[@name='id_categoria']").send_keys(Keys.TAB)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ion-select[@name='id_marca']").send_keys(Keys.TAB)
        time.sleep(3)

        # Dejar campos vacíos y disparar validaciones
        self.driver.find_element(By.XPATH, "//ion-button[text()='Agregar Repuesto']").click()
        time.sleep(3)

        actual1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][1]"))
        ).text
        actual2 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][2]"))
        ).text
        actual3 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][3]"))
        ).text
        actual4 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][4]"))
        ).text
        actual5 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][5]"))
        ).text

        assert (
            actual1 == esperado1 and
            actual2 == esperado2 and
            actual3 == esperado3 and
            actual4 == esperado4 and
            actual5 == esperado5
        ), (
            f"El actual es: '{actual1}' y el esperado es: '{esperado1}', "
            f"El actual es: '{actual2}' y el esperado es: '{esperado2}', "
            f"El actual es: '{actual3}' y el esperado es: '{esperado3}', "
            f"El actual es: '{actual4}' y el esperado es: '{esperado4}', "
            f"El actual es: '{actual5}' y el esperado es: '{esperado5}', "
        )
