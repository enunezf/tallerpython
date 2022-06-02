import logging
import requests
import json

logging.basicConfig(filename='ejemplo_03.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def obtiene_datos():
    try:
        logging.info('Creando una receta')
        URL = 'http://127.0.0.1:8000/recetas/'

        receta = {'nombre':'receta 02', 'descripcion': 'Estas es una receta de pruba desde cliente'}

        r = requests.post(URL, json=receta) 

        data = r.json()

        logging.info('Código de response {}'.format(r.status_code))

        if r.status_code == 200:
            print(data)
            logging.info('Se creo la receta {}'.format(data['id']))
        else:
            logging.warning('No se creo la receta {}'.format(str(data)))
    except Exception as e:
        logging.exception(e)



if __name__ == '__main__':
    obtiene_datos()