#imagen base de Python 3.9
FROM python:3.9-slim

#dependencias del sistema para compilar psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

#directorio de trabajo dentro del contenedor
WORKDIR /app

#dependencias 
COPY requirements.txt .

#instalar las dependencias 
RUN pip install --no-cache-dir -r requirements.txt

#copia el contenido del directorio actual al contenedor
COPY . .

#expone el puerto 9000
EXPOSE 9000

#comando para ejecutar la aplicación FastAPI usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]

