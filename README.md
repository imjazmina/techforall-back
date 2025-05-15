<!--## Instalar python y pip-->

## Instalar y activar el entorno virtual 

**Linux/Mac**
- python3 -m venv .venv
- . .venv/bin/activate<br>
**Windows**
- py -3 -m venv .venv
- .venv\Scripts\activate

## Instalar dependencias
- pip install fastapi uvicorn sqlalchemy sqlite<br>
  o <br>
- pip install -r requirements.txt

## Levantar el proyecto
- uvicorn main:app --reload 

