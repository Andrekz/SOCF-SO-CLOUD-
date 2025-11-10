from flask import Flask

import json
APP = Flask(__name__)

@APP.get("/info")
def info():
        return json.dumps([
            {
                'integrantes':[
                    'André Vnícius Martins de Souza Acosta de Jesus'
                    'Felipe Willian Barros Ferreira'
                    'Luis Gustavo Freitas Kulzer'
                ]
            }
        ])