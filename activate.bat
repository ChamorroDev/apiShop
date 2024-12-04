@echo off

REM Cambiar al directorio del entorno virtual tienda_backend
cd /d "C:\Users\ch\Documents\GitHub\apiShop\entorno-virtualb\Scripts"

REM Activar el entorno virtual
call activate

REM Cambiar al directorio del proyecto
cd /d "C:\Users\ch\Documents\GitHub\apiShop\backend"

REM Ejecutar el servidor Djangoa// segun puerto o 0.0.0.0
python manage.py runserver

