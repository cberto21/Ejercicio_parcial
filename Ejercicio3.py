#Implemente un programa que tenga dos hilos A y B, 
#los dos con acceso a una variable X (global) inicializa la variable en un valor entero aleatorio (entre 1 y 100). 
#El hilo A decrementa X en 1 hasta llegar a 0 intercalando un retardo aleatorio entre 0 y 1 segundo entre cada decremento de X. 
#El hilo B hará iteraciones cada un tiempo aleatorio entre 1 y 4 segundos, imprimiendo el valor de X en cada iteración hasta que X sea 0.
#Tanto A como B deberan imprimir mensajes al arrancar y al terminar, identificando al hilo. El hilo A deberá también indicar el valor inicial de X en el mensaje de arranque o final. 
#Pregunta: Hay condiciones de carrera? Como las evitaria?


import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = random.randint(1, 100)

def hiloAFunc():
    global x
    logging.info(f'Soy {threading.current_thread().name} y el valor de x es {x}')
    while(x != 0):
        x -= 1
        time.sleep(random.randint(0,1))
    logging.info(f'Soy {threading.current_thread().name} y el valor de x es {x}')

def hiloBFunc():

    global x
    logging.info(f'{threading.current_thread().name} arrancó y el valor de x es {x}')
    while(x != 0):
        logging.info(f'El valor de x es {x}')
        time.sleep(random.randint(1,4))

    logging.info(f'Thread {threading.current_thread().name} termino')


def main():
    threadA1 = threading.Thread(target=hiloAFunc)
    threadA2 = threading.Thread(target=hiloAFunc)

    threadB = threading.Thread(target=hiloBFunc)

    threadA1.start()
    threadA2.start()
    threadB.start()

    threadA1.join()
    threadA2.join()
    threadB.join()

if __name__ == '__main__':
    main()
