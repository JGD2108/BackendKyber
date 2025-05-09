# filepath: c:\Users\57304\Documents\Kyber-VPN\kyber-vpn-backend\gunicorn.conf.py
import multiprocessing

# Configuración para producción en Azure
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120