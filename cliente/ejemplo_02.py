import logging
import requests


logging.basicConfig(filename='ejemplo_02.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def obtiene_datos():
    try:
        logging.info('SOLICITANDO INFORMACION DE INTERNET')
        URL = 'http://127.0.0.1:8000/recetas/' 
        r = requests.get(URL) 

        data = r.json()

        logging.info('Código de response {}'.format(r.status_code))

        if r.status_code == 200:
            logging.info('Encontro {} datos'.format(len(data)))
            for element in data:
                print(element['nombre'])
        else:
            logging.warning('No logro obtener datos')
    except Exception as e:
        logging.exception(e)



if __name__ == '__main__':
    obtiene_datos()