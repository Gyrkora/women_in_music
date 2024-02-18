import socket

def start_client(server_host='127.0.0.1', server_port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        with open('log.txt', 'a') as file:  
            file.write(f"nuevo registro con nombre =  'prueba de log'  ")
        s.sendall(b"Hola, servidor. Soy el cliente.")
        data = s.recv(1024)
        print(f"Mensaje recibido del servidor: {data.decode('utf-8')}")

if __name__ == '__main__':
    start_client()


