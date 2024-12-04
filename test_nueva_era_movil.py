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

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_send_input(driver):
#---------------------------------------------------------LOGIN------------------------------------------------------
    #INICIAR SESIÓN
    boton_login = driver.find_element(By.XPATH, '//android.widget.Button[@text="INICIAR SESIÓN"]')
    boton_login.click()
    time.sleep(3)

    #Esperado y Actual
    esperado_codigo = "El campo de codigo es obligatorio."
    actual_codigo = driver.find_element(By.XPATH, '//android.widget.TextView[@text="El campo de codigo es obligatorio."]').text
    assert actual_codigo == esperado_codigo, f"++++++++++ El esperado era '{esperado_codigo}' pero se mostró '{actual_codigo}'"
    print(f"+++++++++++ El esperado '{esperado_codigo}' fue correcto")

    esperado_contraseña = "El campo de contraseña es obligatorio."
    actual_contraseña = driver.find_element(By.XPATH, '//android.widget.TextView[@text="El campo de contraseña es obligatorio."]').text
    assert actual_contraseña == esperado_contraseña, f"++++++++++ El esperado era '{esperado_contraseña}' pero se mostró '{actual_contraseña}'"
    print(f"+++++++++++ El esperado  '{esperado_contraseña}' fue correcto")

    #Codigo
    input_codigo = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-0"]')
    input_codigo.send_keys("pjo599028")
    time.sleep(2)

    #INICIAR SESIÓN
    boton_login = driver.find_element(By.XPATH, '//android.widget.Button[@text="INICIAR SESIÓN"]')
    boton_login.click()
    time.sleep(3)

    #Contraseña
    input_contra = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-1"]')
    input_contra.send_keys("25762734")
    time.sleep(2)

    #INICIAR SESIÓN
    boton_login = driver.find_element(By.XPATH, '//android.widget.Button[@text="INICIAR SESIÓN"]')
    boton_login.click()
    time.sleep(3)

    esperado_codigo = "Credenciales inválidas"
    actual_codigo = driver.find_element(By.XPATH, '//android.widget.TextView[@text="Credenciales inválidas"]').text
    assert actual_codigo == esperado_codigo, f"++++++++++ El esperado era '{esperado_codigo}' pero se mostró '{actual_codigo}'"
    print(f"+++++++++++ El esperado '{esperado_codigo}' fue correcto")

    #Codigo
    input_codigo = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-0"]')
    input_codigo.send_keys("pjo599038")
    time.sleep(2)

    #CodigoCorrecto
    actual_codigo = input_codigo.get_attribute("text")
    esperado_codigo = "pjo599038"
    assert actual_codigo == esperado_codigo, f"++++++++++++El esperado era'{esperado_codigo}' pero se ingresó '{actual_codigo}'."
    print(f"+++++++++++ El esperado '{esperado_codigo}' fue correcto")

    #Contraseña
    input_contra = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-1"]')
    input_contra.send_keys("257627")
    time.sleep(2)

    #Contraseñacorrecta
    actual_contra = input_contra.get_attribute("text")
    esperado_contra = "257627"
    assert actual_contra == esperado_contra, f"++++++++++++El esperado era '{esperado_contra}' pero se ingresó '{actual_contra}'."
    print(f"+++++++++++ El esperado '{esperado_contra}' fue correcto")

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
    
    esperado = "Usuario: pjo599038"
    codigo_usuario = driver.find_element(By.XPATH, '//android.widget.TextView[@text="Usuario: pjo599038"]')

    actual = codigo_usuario.text

    assert actual == esperado, f"++++++++++++ El esperado era '{esperado}' pero se ingresó '{actual}' ."
    print(f"+++++++++++ El usuario esperado '{esperado}' fue correcto ")

#------------------------------------------MENU_CRUDS-----------------------------------------------------
    # Hacer clic en el botón "menu"
    menu_boton = driver.find_element(By.XPATH, '//android.widget.Button[@text="menu"]')
    menu_boton.click()
    time.sleep(3)

    driver.execute_script("mobile: shell", {
    "command": "input",
    "args": ["tap", "44", "439"]
    })
    time.sleep(2) 

    # Hacer clic en "Categorías"
    categorias_elemento = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Categorías"]')
    categorias_elemento.click()
    time.sleep(3) 

    driver.back()  
    time.sleep(3)

#----------------------------------------CRUD_CATEGORIAS------------------------------------------------------  
    # Hacer clic en "RegistrarCategoria"
    categorias_registro = driver.find_element(By.XPATH, '//android.widget.Button[@text="REGISTRAR CATEGORIA"]')
    categorias_registro.click()
    time.sleep(3) 

    # Hacer clic en "RegistrarCategoria"
    categorias_registrar = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR CATEGORIA"]')
    categorias_registrar.click()
    time.sleep(3)

    esperado = "El campo de nombre es obligatorio."
    mensaje_obliga_nombre = driver.find_element(By.XPATH, '//android.widget.TextView[@text="El campo de nombre es obligatorio."]')
    actual = mensaje_obliga_nombre.text
    assert actual == esperado, f"++++++++++++ El esperado era '{esperado}' pero se mostró '{actual}'."
    print(f"+++++++++++ El mensaje esperado '{esperado}' se mostró correctamente.")

    #RegistroNombreCategoria
    nombre_categoria = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-2"]')
    nombre_categoria.send_keys("Minicargadore$")
    time.sleep(2)

    #RegistroDescripcionCategoria
    descrip_categoria = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-3"]')
    descrip_categoria.send_keys("Un minicargador es excelente para cualquier proyecto que implique mover tierra o nivelar el suelo.")
    time.sleep(2)

    # Hacer clic en "RegistrarCategoria"
    categorias_registrar = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR CATEGORIA"]')
    categorias_registrar.click()
    time.sleep(3)

    esperado = "El nombre solo debe contener letras, números, espacios y puntos."
    mensaje_nombre_mal = driver.find_element(By.XPATH, '//android.widget.TextView[@text="El nombre solo debe contener letras, números, espacios y puntos."]')
    actual = mensaje_nombre_mal.text
    assert actual == esperado, f"++++++++++++ El esperado era '{esperado}' pero se mostró '{actual}'."
    print(f"+++++++++++ El mensaje esperado '{esperado}' se mostró correctamente.")

    #RegistroNombreCategoria
    nombre_categoria = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="ion-input-2"]')
    nombre_categoria.send_keys("Minicargadores")
    time.sleep(2)

    # Hacer clic en "RegistrarCategoria"
    categorias_registrar = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR CATEGORIA"]')
    categorias_registrar.click()
    time.sleep(3)

    #deslizar hacia abajo
    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)  
    
    # Hacer clic en "EditarCategoria"
    categorias_editar = driver.find_element(By.XPATH, '(//android.widget.Button[@text="EDITAR"])[5]')
    categorias_editar.click()
    time.sleep(3)  

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
    time.sleep(3)

    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3)
    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)

    #"EliminarCategoria"
    eliminar_categoria = driver.find_element(By.XPATH, '(//android.widget.Button[@text="ELIMINAR"])[5]')
    eliminar_categoria.click()
    time.sleep(3) 

    #"ConfirmarEliminarCategoria"
    eliminar_categoria = driver.find_element(By.XPATH, '//android.widget.Button[@text="SÍ"]')
    eliminar_categoria.click()
    time.sleep(3) 	

    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3)

#------------------------------------------MENU_CRUDS-----------------------------------------------------
    # Hacer clic en el botón "menu"
    menu_boton1 = driver.find_element(By.XPATH, '//android.widget.Button[@text="menu"]')
    menu_boton1.click()
    time.sleep(3)

    driver.execute_script("mobile: shell", {
    "command": "input",
    "args": ["tap", "44", "612"]
    })
    time.sleep(2)  

    # Hacer clic en "Marcas"
    marcas_elemento = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Marcas"]')
    marcas_elemento.click()
    time.sleep(3)

    driver.back()
    time.sleep(3)

#------------------------------------------CRUD_MARCAS-----------------------------------------------------    
    # Hacer clic en "RegistrarMarcas"
    marcas_elemento = driver.find_element(By.XPATH, '//android.widget.Button[@text="REGISTRAR MARCA"]')
    marcas_elemento.click()
    time.sleep(3)

    #RegistroNombreMarca
    marcas_nombre = driver.find_element(By.XPATH, '(//android.widget.EditText)[1]') 
    marcas_nombre.send_keys("VIALERG")
    time.sleep(3)

    # Localizar el botón desplegable de la lista de países
    list_pais_marca = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="ion-sel-0"]')
    list_pais_marca.click()
    time.sleep(2)
    
    #RadioGroup
    radio_list = driver.find_element(By.XPATH, '//android.widget.RadioGroup')
    radio_list.click()
    time.sleep(2)
  
    #ClickPais
    pais_click = driver.find_element(By.XPATH, '(//android.widget.RadioButton[@resource-id and @checked="false"])[2]')
    pais_click.click()
    time.sleep(2)

    #ConfirmarPais
    ok_pais = driver.find_element(By.XPATH, '//android.widget.Button[@text="OK"]')
    ok_pais.click()
    time.sleep(2)

    #RegistrarButtonMarca
    agregar_marca = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR MARCA"]')
    agregar_marca.click()
    time.sleep(3)

    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)

    # Hacer clic en "EditarMarca"
    editar_marca = driver.find_element(By.XPATH, '(//android.widget.Button[@text="EDITAR"])[4]')
    editar_marca.click()
    time.sleep(3)

    #EditarNombreMarca
    marcas_nombre = driver.find_element(By.XPATH, '(//android.widget.EditText)[1]') 
    marcas_nombre.send_keys("")
    time.sleep(3)
    
    #ActualizarMarca
    actualizar_marca = driver.find_element(By.XPATH, '//android.widget.Button[@text="ACTUALIZAR MARCA"]')
    actualizar_marca.click()
    time.sleep(3)

    esperado = "El campo de nombre es obligatorio."
    mensaje_obliga_nombre = driver.find_element(By.XPATH, '//android.widget.TextView[@text="El campo de nombre es obligatorio."]')
    actual = mensaje_obliga_nombre.text
    assert actual == esperado, f"++++++++++++ El esperado era '{esperado}' pero se mostró '{actual}'."
    print(f"+++++++++++ El mensaje esperado '{esperado}' se mostró correctamente.")

    #EditarNombreMarca
    marcas_nombre = driver.find_element(By.XPATH, '(//android.widget.EditText)[1]') 
    marcas_nombre.send_keys("VIALERG$23")
    time.sleep(3)

    #ActualizarMarca
    actualizar_marca = driver.find_element(By.XPATH, '//android.widget.Button[@text="ACTUALIZAR MARCA"]')
    actualizar_marca.click()
    time.sleep(3)

    esperado = "El nombre solo debe contener letras, números, puntos y espacios."
    mensaje_nombre_mal = driver.find_element(By.XPATH, '//android.widget.TextView[@text="El nombre solo debe contener letras, números, puntos y espacios."]')
    actual = mensaje_nombre_mal.text
    assert actual == esperado, f"++++++++++++ El esperado era '{esperado}' pero se mostró '{actual}'."
    print(f"+++++++++++ El mensaje esperado '{esperado}' se mostró correctamente.")

    #EditarNombreMarca
    marcas_nombre = driver.find_element(By.XPATH, '(//android.widget.EditText)[1]') 
    marcas_nombre.send_keys("VIALERG23")
    time.sleep(3)

    #ActualizarMarca
    actualizar_marca = driver.find_element(By.XPATH, '//android.widget.Button[@text="ACTUALIZAR MARCA"]')
    actualizar_marca.click()
    time.sleep(3)

    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3)

    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)

    #EliminarMarca
    eliminar_marca = driver.find_element(By.XPATH, '(//android.widget.Button[@text="ELIMINAR"])[3]')
    eliminar_marca.click()
    time.sleep(3)

    #ConfirmarEliminarMarca
    confirm_eliminar_marca = driver.find_element(By.XPATH, '//android.widget.Button[@text="SÍ"]')
    confirm_eliminar_marca.click()
    time.sleep(3)

    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3)

#----------------------------------------MENU_CRUDS------------------------------------------------------
    #Menu
    menu_boton = driver.find_element(By.XPATH, '//android.widget.Button[@text="menu"]')
    menu_boton.click()
    time.sleep(3)

    driver.execute_script("mobile: shell", {
    "command": "input",
    "args": ["tap", "44", "786"]
    })
    time.sleep(2) 

    #OpcionMenuRepuestos
    opcion_repuestos = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Repuestos"]')
    opcion_repuestos.click()
    time.sleep(3)

    driver.back()
    time.sleep(3)
#----------------------------------------CRUD_REPUESTOS------------------------------------------------------
    #RegistrarRepuesto
    registrar_repuesto = driver.find_element(By.XPATH, '//android.widget.Button[@text="REGISTRAR REPUESTO"]')
    registrar_repuesto.click()
    time.sleep(3)

    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)

    #AgregarRepuesto
    agregar_repuesto = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR REPUESTO"]')
    agregar_repuesto.click()
    time.sleep(3)

    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3)

    mensajes_validacion_repuestos = {
        "El código OEM es obligatorio.": '//android.widget.TextView[@text="El código OEM es obligatorio."]',
        "El campo de nombre es obligatorio.": '//android.widget.TextView[@text="El campo de nombre es obligatorio."]',
        "El número de serie es obligatorio.": '//android.widget.TextView[@text="El número de serie es obligatorio."]',
        "El campo de categoría es obligatorio.": '//android.widget.TextView[@text="El campo de categoría es obligatorio."]',
        "El campo de marca es obligatorio.": '//android.widget.TextView[@text="El campo de marca es obligatorio."]'
    }
    for esperado, xpath in mensajes_validacion_repuestos.items():
        actual = driver.find_element(By.XPATH, xpath).text
        assert actual == esperado, f"++++++++++++ El esperado era '{esperado}' pero se mostró '{actual}'."
        print(f"+++++++++++ El mensaje '{esperado}' se mostró correctamente.")

    #CodigoOEM
    codigo_oem = driver.find_element(By.XPATH, '(//android.widget.EditText)[1]') 
    codigo_oem.send_keys("$$##")
    time.sleep(3)

    #NombreRepuesto
    nombre_repuesto = driver.find_element(By.XPATH, '(//android.widget.EditText)[2]') 
    nombre_repuesto.send_keys("$$##")
    time.sleep(3)

    #NumeroSerie
    numero_serie = driver.find_element(By.XPATH, '(//android.widget.EditText)[3]') 
    numero_serie.send_keys("numerosgod$$##")
    time.sleep(3)

    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)

    #SeleccionCategoriaRepuesto
    list_cate_repuesto = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="ion-sel-2"]')
    list_cate_repuesto.click()
    time.sleep(3)
    
    #RadioGroup
    radio_list1 = driver.find_element(By.XPATH, '//android.widget.RadioGroup')
    radio_list1.click()
    time.sleep(3)
  
    #Clickcate
    cate_click = driver.find_element(By.XPATH, '(//android.widget.RadioButton[@resource-id and @checked="false"])[4]')
    cate_click.click()
    time.sleep(3)

    #Confirmarcate
    ok_cate_repu = driver.find_element(By.XPATH, '//android.widget.Button[@text="OK"]')
    ok_cate_repu.click()
    time.sleep(3)

    #SeleccionMarcaRepuesto
    list_marca_repuesto = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="ion-sel-3"]')
    list_marca_repuesto.click()
    time.sleep(3)
    
    #RadioGroup
    radio_list2 = driver.find_element(By.XPATH, '//android.widget.RadioGroup')
    radio_list2.click()
    time.sleep(3)
  
    #Clickmarca
    marca_click = driver.find_element(By.XPATH, '(//android.widget.RadioButton[@resource-id and @checked="false"])[1]')
    marca_click.click()
    time.sleep(3)

    #Confirmarmarca
    ok_marca_repu = driver.find_element(By.XPATH, '//android.widget.Button[@text="OK"]')
    ok_marca_repu.click()
    time.sleep(3)

    #AgregarRepuesto
    agregar_repuesto1 = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR REPUESTO"]')
    agregar_repuesto1.click()
    time.sleep(3)

    driver.swipe(start_x=540, start_y=500, end_x=540, end_y=2000, duration=1000)
    time.sleep(3) 

    mensajes_validaciones2_repuestos = {
    "El código OEM es invalido.": '//android.widget.TextView[@text="El código OEM es invalido."]',
    "El nombre solo debe contener letras, números, puntos y espacios.": '//android.widget.TextView[@text="El nombre solo debe contener letras, números, puntos y espacios."]',
    "El número de serie es invalido.": '//android.widget.TextView[@text="El número de serie es invalido."]'
    }
    for esperado, xpath in mensajes_validaciones2_repuestos.items():
        actual = driver.find_element(By.XPATH, xpath).text
        assert actual == esperado, f"++++++++++++ El esperado era '{esperado}' pero se mostró '{actual}'."
        print(f"+++++++++++ El mensaje '{esperado}' se mostró correctamente.")

    #CodigoOEM
    codigo_oem = driver.find_element(By.XPATH, '(//android.widget.EditText)[1]') 
    codigo_oem.send_keys("6L3Z3280B")
    time.sleep(3)

    #NombreRepuesto
    nombre_repuesto = driver.find_element(By.XPATH, '(//android.widget.EditText)[2]') 
    nombre_repuesto.send_keys("Pastillas de freno")
    time.sleep(3)

    #NumeroSerie
    numero_serie = driver.find_element(By.XPATH, '(//android.widget.EditText)[3]') 
    numero_serie.send_keys("90331232")
    time.sleep(3)

    driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=1000)
    time.sleep(3)
    
    #AgregarRepuesto
    agregar_repuesto1 = driver.find_element(By.XPATH, '//android.widget.Button[@text="AGREGAR REPUESTO"]')
    agregar_repuesto1.click()
    time.sleep(3)

    for _ in range(30):
        driver.swipe(start_x=540, start_y=2000, end_x=540, end_y=500, duration=200)
        time.sleep(1)
    
    #ClickDetalle
    detalle_repuesto = driver.find_element(By.XPATH, '(//android.widget.Button[@text="DETALLE"])[3]')
    detalle_repuesto.click()
    time.sleep(4)

    driver.back()
    time.sleep(3)
#----------------------------------------MENU_CRUDS------------------------------------------------------
    # Hacer clic en el botón "menu"
    menu_boton = driver.find_element(By.XPATH, '//android.widget.Button[@text="menu"]')
    menu_boton.click()
    time.sleep(3)

    driver.execute_script("mobile: shell", {
    "command": "input",
    "args": ["tap", "44", "269"]
    })
    time.sleep(2) 
#----------------------------------------INICIO------------------------------------------------------
    # Hacer clic en el Inicio
    menu_inicio = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Inicio"]')
    menu_inicio.click()
    time.sleep(3)

    driver.back()
    time.sleep(3)
#----------------------------------------CIERRE_SESION------------------------------------------------------
    #Cerrar Sesion
    menu_inicio = driver.find_element(By.XPATH, '//android.webkit.WebView[@text="Nueva Era WebPage"]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')
    menu_inicio.click()
    time.sleep(4)


    

    

    


    

    













    








