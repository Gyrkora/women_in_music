# server.py
import socket

def start_server(host='127.0.0.1', port=65432):
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
                print(f"Mensaje recibido del servidor: {data.decode('utf-8')}")
                conn.sendall(b"Mensaje recibido. Gracias.")
                break 

if __name__ == '__main__':
    start_server()
