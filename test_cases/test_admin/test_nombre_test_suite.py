# Incluir acá los test cases para el módulo específico.

from page_elements.admin_page.modulo_pagina_page import AdminPage
def test_uni():
    admin = AdminPage()
    admin.ejecutar_login()
    print("CRUD EMPLEADOS")
