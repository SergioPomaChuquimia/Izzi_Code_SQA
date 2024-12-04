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
        
    def test_deta_empleados(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-menu-button[contains(@class, 'buttons-men')]"))
        ).click()
        time.sleep(3)

        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-item[@routerlink='/empleados']"))
        ).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-button[.//ion-icon[@name='close-outline']]"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ion-item[ion-label[h2[text()='ADMINISTRADOR'] and p[contains(text(), 'Nombres: RRR')]]]//p[contains(text(), 'Apellidos:')]"))
        )
        actual = self.driver.find_element(By.XPATH, "//ion-item[ion-label[h2[text()='ADMINISTRADOR'] and p[contains(text(), 'Nombres: RRR')]]]//p[contains(text(), 'Apellidos:')]").text
        print("++++++++", actual)
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ion-item[ion-label//p[contains(text(), 'Apellidos: RR')]]//ion-button[text()='Detalle']"))
        ).click()
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ion-item[ion-label[h2[text()='ADMINISTRADOR'] and p[contains(text(), 'Nombres: RRR')]]]//p[contains(text(), 'Apellidos:')]"))
        )
        actual2 = self.driver.find_element(By.XPATH, "//button[contains(@class, 'action-sheet-button') and .//span[contains(text(), 'Apellidos:')]]").text
        print("-----------", actual2)
        time.sleep(3)
        if actual2 == actual:
            print("Los apellidos coinciden en el detalle")
        else:
            print("NO coinciden los apellidos en el detalle")
        
        
        print("CRUD EMPLEADOS222")
        self.driver.quit()  # FINNN



   
