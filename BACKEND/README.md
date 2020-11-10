# webApp_RPA
Aplicacion que servira de interaccion para un proyecto de RPA (UiPath)

## Instalar
Flask
    
    pip install Flask
    
SQLite3
    
    sudo apt-get update
    sudo apt-get install sqlite3
    sqlite3 --version
    
## Run app
 Primero darle permisos para ejecutar
 
    chmod 777 run.sh
    
 Para ejecutar correr lo siguiente
    
    sh ./run.sh
    
## Resetear BD
 Solo ejecutar el siguiente comando
 
    python3 init_db.py
    
## Construir la imagen

    docker build -t webapp .
    docker run -it -d -p 80:80 --name=RPA webapp
    
## Usando la imagen del repositorio
    
    docker pull yoseanne/webapp:[tag]
    docker run -it -d -p 80:80 --name=RPA yoseanne/webapp    
 