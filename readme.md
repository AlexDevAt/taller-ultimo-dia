En caso que tengan alguna duda o ocupen ayuda en algun tea similar, 
les dejo mi ig: alexgonzct

1. Clonar el repositorio

git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
cd TU-REPOSITORIO

Reemplaza la URL con la dirección de tu repositorio.

2. Crear un entorno virtual

python -m venv .venv

3. Activar el entorno virtual

macOS / Linux

source .venv/bin/activate

Windows (PowerShell)

.venv\Scripts\Activate.ps1

4. Instalar las dependencias

python -m pip install -r requirements.txt

5. Ejecutar el servidor

fastapi dev main.py

El servidor estará disponible en:

API: http://127.0.0.1:8000

Documentación interactiva: http://127.0.0.1:8000/docs

Documentación alternativa: http://127.0.0.1:8000/redoc