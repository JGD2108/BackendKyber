#!/bin/bash

# Configurar variables de entorno
export PYTHONPATH=/home/site/wwwroot

# Activar entorno virtual si existe
if [ -d /home/site/wwwroot/env ]; then
    source /home/site/wwwroot/env/bin/activate
fi

# Aplicar migraciones si es necesario
# python app/db_migrations.py

# Iniciar la aplicación con gunicorn
gunicorn app.main:app --config gunicorn.conf.py