# Arquitectura Maestro-Trabajadores en Python

Este proyecto implementa una arquitectura Maestro-Trabajadores utilizando Python. Un servidor maestro recibe tareas de un cliente a través de sockets, las procesa en paralelo utilizando `multiprocessing`, y devuelve los resultados al cliente.

## Requisitos

- Python 3.6 o superior
- No es necesario instalar librerías externas. Se utilizan únicamente módulos estándar: `socket`, `pickle`, `multiprocessing`.

## Archivos incluidos

- `servidor_maestro.py`: Servidor que actúa como maestro. Recibe los datos, los procesa en paralelo y devuelve el resultado.
- `cliente.py`: Cliente que envía una lista de números al servidor.
- `README.md`: Instrucciones de uso.

## Instrucciones de ejecución

### 1. Iniciar el servidor

Abrir una terminal y ejecutar el siguiente comando:

```bash
python servidor_maestro.py

### 2. Ejecutar el cliente

Abrir otro terminal y ejecutar:
python ciente.py

### Ejemplo de salida

[CLIENTE] Enviando datos: [2, 3, 4, 5]
[CLIENTE] Resultados recibidos: [4, 9, 16, 25]
