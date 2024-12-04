import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_elements.admin_page.modulo_login_page import AdminPage


class TestValidacionRepuesto:
    def setup_method(self):
        admin = AdminPage()
        self.driver = admin.ejecutar_login()
        print("Iniciando pruebas de validación en el módulo de repuestos")
        time.sleep(3)

    def teardown_method(self):
        print("Pruebas de validación completadas")
        self.driver.quit()

    def test_val(self):
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

        esperado1 = "El código OEM es invalido."
        esperado2 = "El nombre solo debe contener letras, números, puntos y espacios."
        esperado3 = "El número de serie es invalido."
        esperado4 = "La cantidad en stock debe ser un valor positivo."
        esperado5 = "El campo de categoría es obligatorio."
        esperado6 = "El campo de marca es obligatorio."
        esperado7 = "El costo unitario debe tener un valor positivo."

        self.driver.find_element(By.XPATH, "//input[@name='codigo_oem']").send_keys("#@$@5$#@")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("#@$@5$#@")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='numero_serie']").send_keys("#@$@5$#@")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_stock']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_stock']").send_keys("0")
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_stock']").send_keys(Keys.TAB)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ion-select[@name='id_categoria']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//input[@name='costo_unitario']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='costo_unitario']").send_keys("0")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ion-button[text()='Agregar Repuesto']").click()
        time.sleep(3)

        actual1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][1]"))
        ).text
        actual2 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][2]"))
        ).text
        actual3 = self.driver.find_element(By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][3]").text
        actual4 = self.driver.find_element(By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][4]").text
        actual5 = self.driver.find_element(By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][5]").text
        actual6 = self.driver.find_element(By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][6]").text
        actual7 = self.driver.find_element(By.XPATH, "//div[@style='color: red; margin-bottom: 10px; text-align: center;'][7]").text
        assert (
            actual1 == esperado1 and
            actual2 == esperado2 and
            actual3 == esperado3 and
            actual4 == esperado4 and
            actual5 == esperado5 and
            actual6 == esperado6 and
            actual7 == esperado7
        ), (
            f"El actual es: '{actual1}' y el esperado es: '{esperado1}', "
            f"El actual es: '{actual2}' y el esperado es: '{esperado2}', "
            f"El actual es: '{actual3}' y el esperado es: '{esperado3}', "
            f"El actual es: '{actual4}' y el esperado es: '{esperado4}', "
            f"El actual es: '{actual5}' y el esperado es: '{esperado5}', "
            f"El actual es: '{actual6}' y el esperado es: '{esperado6}', "
            f"El actual es: '{actual7}' y el esperado es: '{esperado7}', "
        )
