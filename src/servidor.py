"""
Módulo que contiene a la función da inicio al servidor con protocolo TCP/IP 

"""


import socket





def iniciar_servidor(host='127.0.0.1', port=65432):

    """ 
    Al ejecutarse se crea un socket que dará apertura al servidor a recibir y enviar mensajes a clientes

    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Servidor escuchando en {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Conectado por {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"conexión desde servidor: {data.decode('utf-8')}")
                conn.sendall(b"servidor conectado.")
                break 

if __name__ == '__main__':
    iniciar_servidor()
