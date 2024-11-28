from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class AdminPage:
    def ejecutar_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get('http://localhost:8100/login')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='ion-input-0']"))
            ).send_keys("rafcoronelc@gmail.com")
            time.sleep(3)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='ion-input-1']"))
            ).send_keys("password123")
            time.sleep(3)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ion-button[@type='submit' and contains(text(), 'Iniciar Sesión')]"))
            ).click()
            time.sleep(3)
            return driver  
        except Exception as e:
            print("Se produjo un error")
            

