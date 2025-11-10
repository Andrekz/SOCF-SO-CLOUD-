from flask import Flask
import os
import psutil
import platform
import json

APP = Flask(__name__)

@APP.get("/info")
def info():
        return json.dumps([
            {
                'integrantes':[
                    'André Vnícius Martins de Souza Acosta de Jesus',
                    'Felipe Willian Barros Ferreira',
                    'Luis Gustavo Freitas Kulzer'
                ]
            }
        ])

@APP.get("/metricas")
def metricas():
    xpid = os.getpid()
    xprocesso = psutil.Process(xpid)
    xmemoria = xprocesso.memory_info().rss / 1024 / 1024
    xcpu = psutil.cpu_percent(interval=1)
    xsistema = platform.platform()
    
    return json.dumps({
        'integrantes': [
            'André Vnícius Martins de Souza Acosta de Jesus',
            'Felipe Willian Barros Ferreira',
            'Luis Gustavo Freitas Kulzer'
        ],
        'pid': xpid,
        'memoria_usada': round(xmemoria, 2),
        'cpu': xcpu,
        'sistema_operacional': xsistema
    })

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)