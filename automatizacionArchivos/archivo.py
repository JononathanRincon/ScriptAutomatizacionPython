import os
# 1. Ruta raiz donde se encuentra ubicado
cmd  = os.getcwd() 
# 2. Crear Carpeta dentro de un directorio
NombreCarpeta = "CarpetaEjemplo1"
path = os.path.join(cmd,NombreCarpeta)
## Linea de codigo comentada -- os.mkdir(path) 
# Ruta de todos los archivos que se encuentran en la carpeta
# 3. Crea Carpetas dentro de un directorio, sino existe la ruta de carpetas, aun asi las crea todas
# os.makedirs(path) 