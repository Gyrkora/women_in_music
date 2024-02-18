"""
Módulo que implementa la comunicación de red para la aplicación mediante sockets. Su clase incluye métodos para iniciar y apagar el servidor, lanzar el servidor como un proceso en segundo plano y manejar la conexión del cliente.  


"""


import socket
import subprocess
import threading
import sys
import os
from pathlib import Path

theproc = None

class Servidor():


    """ 
    Clase que se encarga de la gestión de crear y mantener la conexión servidor-cliente

    """

    def __init__(self) -> None:
        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz, 'src', 'servidor.py')
        self.ruta_cliente = os.path.join(self.raiz,  'servidor_cliente_sockets.py')
        self.proceso_servidor = None

    
        """ 
        inicia la conexión con el servidor
        
        """

    def iniciar_conexion(self):
        global theproc
        if theproc is not None:
            self.apagar_servidor()
        threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()

    

        """ 
        Comienza con el proceso de conexión con el servidor al ejecutar el archivo
        
        """
            
    def lanzar_servidor(self, var):
        global theproc
        the_path_server = self.ruta_server
        if var == True:
            theproc = subprocess.Popen([sys.executable, the_path_server])
            theproc.communicate()


        
        """ 
        Apaga el servidor 
        
        """

    def apagar_servidor(self):
        global theproc
        if theproc is not None:  
            try:
                theproc.terminate()  # Termina el proceso
                theproc.wait()
                theproc = None  
                print("Servidor apagado")
            except Exception as e:
                print(f"Error al intentar apagar el servidor: {e}")


         
    
        """ 
        Inicia la conexión con el  cliente al ejectutar el archivo correspondiente
        
        """

    def iniciar_conexion_cliente(self, var):
        global theproc
        the_path_cliente = self.ruta_cliente
        if var == True:
            theproc = subprocess.Popen([sys.executable, the_path_cliente])
            theproc.communicate()


    
        """ 
        Se consolida la conexión y se envían mensajes con el servidor 
        
        """

    def conexion_cliente(self ,info, server_host='127.0.0.1', server_port=65432):
        self.iniciar_conexion()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_host, server_port))
            with open('log.txt', 'a') as file: 
                if isinstance(info, int):
                    file.write(f"(Servidor) Hubo un cambio en el id = {info}  \n")  
                else:
                    file.write(f"(Servidor) Hubo un cambio de nombre = {info} de un registro   \n")
            s.sendall(b"cliente conectado")
            data = s.recv(1024)
            print(f"conexión desde cliente: {data.decode('utf-8')}")          