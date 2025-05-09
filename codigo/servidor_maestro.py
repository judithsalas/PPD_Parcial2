# servidor_maestro.py
import socket
import pickle
import threading
from multiprocessing import Pool

HOST = 'localhost'
PORT = 5000

def procesar_tarea(args):
    num, operacion = args
    if operacion == 'cuadrado':
        return num ** 2
    elif operacion == 'cubo':
        return num ** 3
    else:
        raise ValueError("Operación no válida")

def manejar_cliente(conn, addr):
    print(f"[SERVIDOR] Conexión establecida con {addr}")
    try:
        data = conn.recv(4096)
        payload = pickle.loads(data)

        numeros = payload.get("numeros", [])
        operacion = payload.get("operacion", "cuadrado")

        print(f"[SERVIDOR] Datos recibidos de {addr}: {numeros} (operación: {operacion})")

        tareas = [(num, operacion) for num in numeros]

        with Pool() as pool:
            resultados = pool.map(procesar_tarea, tareas)

        conn.sendall(pickle.dumps(resultados))
        print(f"[SERVIDOR] Resultados enviados a {addr}: {resultados}")
    except Exception as e:
        print(f"[ERROR] Conexión con {addr} falló: {e}")
    finally:
        conn.close()
        print(f"[SERVIDOR] Conexión cerrada con {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVIDOR] Escuchando en {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            hilo_cliente = threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True)
            hilo_cliente.start()

if __name__ == "__main__":
    main()
