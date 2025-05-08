FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias de compilación para pyoqs
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY ./app /app/app

# Exponer puertos para la API y el servicio VPN
EXPOSE 8000 1194

# Comando para iniciar el servicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
