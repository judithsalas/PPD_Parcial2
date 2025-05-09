# servidor_maestro.py
import socket
import pickle
from multiprocessing import Pool

HOST = 'localhost'
PORT = 5000

def procesar_tarea(x):
    return x ** 2

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVIDOR] Esperando conexiones en {HOST}:{PORT}...")

        conn, addr = s.accept()
        with conn:
            print(f"[SERVIDOR] Conectado con {addr}")
            data = conn.recv(4096)
            numeros = pickle.loads(data)
            print(f"[SERVIDOR] Datos recibidos: {numeros}")

            with Pool() as pool:
                resultados = pool.map(procesar_tarea, numeros)

            print(f"[SERVIDOR] Resultados procesados: {resultados}")
            conn.sendall(pickle.dumps(resultados))

if __name__ == "__main__":
    main()
