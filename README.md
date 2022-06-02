# Taller de python

## Preparación

### Ambiente virtual

Crear ambiente

```
# python3 -m venv [nombre ambiente virtual]
python3 -m venv venv
```

Activar ambiente

```
# linux / mac
source venv/bin/activate

# windows
.\venv\Scripts\activate
```

Desactivar Ambiente

```
deactivate
```

### Instalar librerías

Para instalar un librería

```
# pip install libreria
pip install fastapi
```

Para instalar todas las librerías de un proyecto

```
pip install -r requirements.txt
# En vi versión de windows la instalación con pip falla, lo solucione con
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```



Listar librerías

```
pip list
Package            Version
------------------ -----------
anyio              3.6.1
asgiref            3.5.2
certifi            2022.5.18.1
charset-normalizer 2.0.12
click              8.1.3
```
