import requests  #Importamos la librería requests

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
URL = 'http://127.0.0.1:8000/recetas/' 
#solicitamos la información y guardamos la respuesta en data.
data = requests.get(URL) 

data = data.json() #convertimos la respuesta en dict

for element in data: #iteramos sobre data
    print(element['nombre']) #Accedemos a sus valores