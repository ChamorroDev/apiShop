@echo off

REM Cambiar al directorio del entorno virtual tienda_backend
cd /d "C:\Users\ch\Desktop\proyecto\api\tienda_backend\Scripts"

REM Activar el entorno virtual
call activate

REM Cambiar al directorio del proyecto
cd /d "C:\Users\ch\Desktop\proyecto\api\backend"

REM Ejecutar el servidor Djangoa// segun puerto o 0.0.0.0
python manage.py runserver

