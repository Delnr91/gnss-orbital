# Usa una imagen oficial y ligera de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del backend
COPY backend/ ./backend/

# Exponer el puerto (Koyeb/Render usan el puerto por defecto o lo inyectan via variable de entorno)
EXPOSE 8000

# Comando para iniciar la API
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
