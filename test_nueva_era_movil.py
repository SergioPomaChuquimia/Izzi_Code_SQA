import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "DI7PTSGUTG85HIPF"
    options.app_package = "com.nuevaera.app"
    options.app_activity = ".MainActivity"
    options.new_command_timeout = 600
    options.adbExecTimeout = 120000
    options.connect_hardware_keyboard = True

    # Conexión con Appium
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_send_input(driver):
    #Codigo
    input_codigo = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-0"]')
    input_codigo.send_keys("pjo599038")
    time.sleep(2)

    #Contraseña
    input_password = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-1"]')
    input_password.send_keys("257627")
    time.sleep(2)

    #Verificacion Login
    assert input_codigo.get_attribute("text") == "pjo599038"
    assert input_password.get_attribute("text") == "257627"

    #OjoContraVer
    imagen_elemento = driver.find_element(By.XPATH, '//android.widget.Image')
    imagen_elemento.click()
    time.sleep(2)

    #OjoContraOcultar
    imagen_elemento = driver.find_element(By.XPATH, '//android.widget.Image')
    imagen_elemento.click()
    time.sleep(2) 

    #INICIAR SESIÓN
    boton_login = driver.find_element(By.XPATH, '//android.widget.Button[@text="INICIAR SESIÓN"]')
    boton_login.click()
    time.sleep(3) 

    # Hacer clic en el botón "menu"
    menu_boton = driver.find_element(By.XPATH, '//android.widget.Button[@text="menu"]')
    menu_boton.click()
    time.sleep(5)

    # Hacer clic en "Categorías"
    categorias_elemento = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Categorías"]')
    categorias_elemento.click()
    time.sleep(6) 

    driver.back()  
    time.sleep(3)  

    # Hacer clic en "RegistrarCategoria"
    categorias_registro = driver.find_element(By.XPATH, '//android.widget.Button[@text="REGISTRAR CATEGORIA"]')
    categorias_registro.click()
    time.sleep(6) 

    #RegistroNombreCategoria
    nombre_categoria = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-2"]')
    nombre_categoria.send_keys("Minicargadores")
    time.sleep(2)

    #RegistroDescripcionCategoria
    descrip_categoria = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-3"]')
    descrip_categoria.send_keys("Un minicargador es excelente para cualquier proyecto que implique mover tierra o nivelar el suelo.")
    time.sleep(2)

    # Hacer clic en "RegistrarCategoria"
    categorias_registrar = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR CATEGORIA"]')
    categorias_registrar.click()
    time.sleep(4)  # Espera de 2 segundos

    #deslizar hacia abajo
    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(6)  
    
    # Hacer clic en "EditarCategoria"
    categorias_editar = driver.find_element(By.XPATH, '(//android.widget.Button[@text="EDITAR"])[5]')
    categorias_editar.click()
    time.sleep(4)  

    #EditarNombreCategoria
    nombre_editcategoria = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-4"]')
    nombre_editcategoria.send_keys("Manipuladores telescópicos")
    time.sleep(2)

    #EditarDescripcionCategoria
    descrip_editcategoria = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-5"]')
    descrip_editcategoria.send_keys("Esto minimiza el tiempo y el esfuerzo al transportar materiales.")
    time.sleep(2)

    # Confirmar "EditarCategoria"
    confirm_editar = driver.find_element(By.XPATH, '//android.widget.Button[@text="ACTUALIZAR CATEGORIA"]')
    confirm_editar.click()
    time.sleep(4)

    #deslizar hacia arriba
    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3)

    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)

    #"EliminarCategoria"
    eliminar_categoria = driver.find_element(By.XPATH, '(//android.widget.Button[@text="ELIMINAR"])[5]')
    eliminar_categoria.click()
    time.sleep(4) 

    #"ConfirmarEliminarCategoria"
    eliminar_categoria = driver.find_element(By.XPATH, '//android.widget.Button[@text="SÍ"]')
    eliminar_categoria.click()
    time.sleep(4) 	

    #deslizar hacia arriba
    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3) 

    # Hacer clic en "RegistrarCategoria"
    categorias_registro2 = driver.find_element(By.XPATH, '//android.widget.Button[@text="REGISTRAR CATEGORIA"]')
    categorias_registro2.click()
    time.sleep(6)

    # Hacer clic en "CerrarModalCategoria"
    cerrar_modal_categoria_registro = driver.find_element(By.XPATH, '//android.widget.Button[@text="CERRAR"]')
    cerrar_modal_categoria_registro.click()
    time.sleep(4)

    # Hacer clic en "EditarCategoria"
    categorias_editar = driver.find_element(By.XPATH, '(//android.widget.Button[@text="EDITAR"])[1]')
    categorias_editar.click()
    time.sleep(4)  

    # Hacer clic en "CerrarModalCategoriaEdit"
    cerrar_modal_categoria_edit = driver.find_element(By.XPATH, '//android.widget.Button[@text="CERRAR"]')
    cerrar_modal_categoria_edit.click()
    time.sleep(4)

    # Hacer clic en el botón "menu"
    menu_boton1 = driver.find_element(By.XPATH, '//android.widget.Button[@text="menu"]')
    menu_boton1.click()
    time.sleep(5) 

    # Hacer clic en "Marcas"
    marcas_elemento = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Marcas"]')
    marcas_elemento.click()
    time.sleep(4)

    driver.back()
    time.sleep(3)

    # Hacer clic en "RegistrarMarcas"
    marcas_elemento = driver.find_element(By.XPATH, '//android.widget.Button[@text="REGISTRAR MARCA"]')
    marcas_elemento.click()
    time.sleep(6)

    #RegistroNombreMarca
    marcas_nombre = driver.find_element(By.XPATH, '(//android.widget.EditText)[1]') 
    marcas_nombre.send_keys("VIALERG")
    time.sleep(6)

    # Localizar el botón desplegable de la lista de países
    list_pais_marca = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="ion-sel-0"]')
    list_pais_marca.click()
    time.sleep(4)
    
    #RadioGroup
    radio_list = driver.find_element(By.XPATH, '//android.widget.RadioGroup')
    radio_list.click()
    time.sleep(4)
  
    #ClickPais
    pais_click = driver.find_element(By.XPATH, '(//android.widget.RadioButton[@resource-id and @checked="false"])[2]')
    pais_click.click()
    time.sleep(6)

    #ConfirmarPais
    list_pais_marca = driver.find_element(By.XPATH, '//android.widget.Button[@text="OK"]')
    list_pais_marca.click()
    time.sleep(4)

    #RegistrarButtonMarca
    list_pais_marca = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR MARCA"]')
    list_pais_marca.click()
    time.sleep(4)

    #RegistroEmailMarca
    marcas_email = driver.find_element(By.XPATH, '//android.widget.EditText)[1]')
    marcas_email.send_keys("Info@vialerg.com.ar")
    time.sleep(4)
         
    #RegistroDireccionMarca
    marcas_direccion = driver.find_element(By.XPATH, '//android.widget.EditText)[2]')
    marcas_direccion.send_keys("Lavalle 1430 3ºA, Capital Federal, Buenos Aires, Argentina.")
    time.sleep(4)
     
    #RegistroSitioWebMarca
    marcas_web = driver.find_element(By.XPATH, '//android.widget.EditText)[3]')
    marcas_web.send_keys("https://vialerg.com.ar/")
    time.sleep(4)

    #RegistroDescripcionMarca
    marcas_descripcion = driver.find_element(By.XPATH, '//android.widget.EditText)[4]')
    marcas_descripcion.send_keys("VIALERG se dedica a la fabricación y comercialización de maquinaria pesada")
    time.sleep(4)




