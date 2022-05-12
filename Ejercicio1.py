#Implemente un programa que ejecute 10 hilos que impriman un mensaje identificando al hilo,
# luego esperen un tiempo aleatorio entre 1 y 
#5 segundos y luego impriman un mensaje indicando que terminaron (identificando al hilo)

import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def imprimir():
    logging.info(f'Arrancó {threading.current_thread().name}, somos {threading.active_count()} threads' )
    time.sleep(random.randint(1,5))
    logging.info(f'Terminó {threading.current_thread().name}, somos {threading.active_count()} threads')

if __name__ == '__main__':
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=imprimir))

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()