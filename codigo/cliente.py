# cliente.py
import socket
import pickle

HOST = 'localhost'
PORT = 5000

def main():
    numeros = [2, 3, 4, 5]
    print(f"[CLIENTE] Enviando datos: {numeros}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(pickle.dumps(numeros))
        data = s.recv(4096)

    resultados = pickle.loads(data)
    print(f"[CLIENTE] Resultados recibidos: {resultados}")

if __name__ == "__main__":
    main()
