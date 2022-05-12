#Modifique el programa anterior de modo que pueda medir e 
#imprimir el tiempo total que tomo ejecutarse cada hilo (en milisengundos)

import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def imprimir():
    inicio = time.perf_counter()
    logging.info(f'Arrancó {threading.current_thread().name}' )
    time.sleep(random.randint(1,5))
    logging.info(f'Terminó {threading.current_thread().name}')
    logging.info(f'La thread {threading.current_thread().name} demoro {time.perf_counter() - inicio} segundos')

if __name__ == '__main__':
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=imprimir))

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()