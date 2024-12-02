Configuración de Appium con Python

Requisitos Previos
1. Instalar Node.js
  Verifica que Node.js esté instalado ejecutando:
   node -v
   npm -v
2. Instalar Appium
  Instala Appium globalmente con:
   npm install -g appium
   appium -v
  Luego, instala el driver uiautomator2:
   appium driver install uiautomator2
3. Descargar Appium Inspector
  Descarga la herramienta gráfica para inspeccionar elementos de la interfaz:
   https://github.com/appium/appium-inspector/releases
4. Instalar Android Studio
  Asegúrate de que los siguientes SDK estén configurados:
  - Platform-Tools
  - Build-Tools
  - Emulator
  Agrega el directorio platform-tools a las variables de entorno PATH.
5. Verificar adb
  Comprueba que adb esté funcionando:
   adb version

Configuración del Dispositivo
6. Conectar el Móvil
  Activa la Depuración USB en tu dispositivo Android.
7. Verificar Conexión del Dispositivo
  Usa el comando para comprobar que el dispositivo esté conectado:
   adb devices

Configuración de Python
8. Instalar Python
  Asegúrate de tener Python instalado.
9. Instalar Dependencias de Python
  Instala los siguientes paquetes necesarios:
   pip install Appium-Python-Client
   pip install selenium
   pip install pytest
   pip install webdriver-manager

Uso de Appium
10. Iniciar el Servidor Appium
  Ejecuta el servidor Appium con opciones de seguridad relajadas:
   appium --allow-insecure chromedriver_autodownload --relaxed-security
11. Ejecutar Appium Inspector
  Abre el Appium Inspector para inspeccionar y configurar la automatización.
Configuración del Inspector
 - Listar paquetes instalados en el dispositivo:
   adb shell pm list packages | grep nuevaera
 - Obtener actividad de la app actual:
   adb shell dumpsys window | findstr "mCurrentFocus mFocusedApp"

Parámetros para el Inspector
Usa esta configuración para conectar el Inspector a tu dispositivo:
{
  "platformName": "Android",
  "appium:deviceName": "DI7PTSGUTG85HIPF",
  "appium:appPackage": "com.nuevaera.app",
  "appium:appActivity": ".MainActivity",
  "appium:appWaitActivity": ".MainActivity, com.nuevaera.app.*",
  "appium:automationName": "UiAutomator2",
  "appium:newCommandTimeout": 600,
  "appium:adbExecTimeout": 120000,
  "appium:connectHardwareKeyboard": true
}