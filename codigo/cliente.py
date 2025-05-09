# cliente.py
import socket
import pickle

HOST = 'localhost'
PORT = 5000

def main():
    numeros = [2, 3, 4, 5]
    operacion = 'cubo'  # puedes poner 'cuadrado' o 'cubo'

    print(f"[CLIENTE] Enviando datos: {numeros} (operación: {operacion})")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        payload = {
            "numeros": numeros,
            "operacion": operacion
        }
        s.sendall(pickle.dumps(payload))
        data = s.recv(4096)

    resultados = pickle.loads(data)
    print(f"[CLIENTE] Resultados recibidos: {resultados}")

if __name__ == "__main__":
    main()
