import os
# 1. Ruta raiz donde se encuentra ubicado
cmd  = os.getcwd() 
# 2. Crear Carpeta dentro de un directorio
NombreCarpeta = "CarpetaEjemplo1"
path = os.path.join(cmd,NombreCarpeta)
# validar si la carpeta existe
if os.path.exists(path):    
    print(f"Carpeta '{NombreCarpeta}' ya existe en {cmd}")    
else:
    # crear carpeta
    os.mkdir(path)
    print(f"Carpeta '{NombreCarpeta}' creada en {cmd}")
# 3. Crea Carpetas dentro de un directorio, sino existe la ruta de carpetas, aun asi las crea todas
# os.makedirs(path) 
# 4. Devuelve un diccion de los archivos que se encuentran en la carpeta
# 4. Devuelve una lista de los archivos que se encuentran en la carpeta "automationArchivos"
automation_folder = os.path.join(cmd, "automatizacionArchivos")
# valida si existe la ruta y si la ruta es una direccion de carpeta
if os.path.exists(automation_folder) and os.path.isdir(automation_folder):
    #Devuelve una lista de los archivos que se encuentran guardados
    listaDireccion = os.listdir(automation_folder)
    print("Archivos en 'automationArchivos':", listaDireccion)
else:
    print(f"La carpeta 'automationArchivos' no existe en {cmd}")
    # Crear la carpeta si no existe
    os.makedirs(automation_folder, exist_ok=True)
    print(f"Carpeta 'automationArchivos' creada en {cmd}")

# Elimina directorios o archivos
# Eliminar archivos que se encontraban en la carpeta 
path2 = os.path.join(automation_folder,listaDireccion[1])
archivos = os.listdir(path2)
for archivo in archivos:
    pathArchivo = os.path.join(path2,archivo)
    os.remove(pathArchivo)
    print(f"Archivo '{archivo}' eliminado")
    
# Eliminar carpetas vacias
os.rmdir(path2)
# Renombra archivo 
os.rename("archivo.txt")
