import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
platosDisponibles = 3
semaphore = threading.Semaphore(platosDisponibles)
gateway = threading.Semaphore(1)
class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    global semaphore
    global gateway
    while (True): 
        gateway.acquire()
        logging.info('Reponiendo los platos...')
        platosDisponibles = 3
        time.sleep(3)#sleep para poder hacer seguimiento del bucle mientras lo corrijo
        semaphore.release()
      
class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    global semaphore
    global gate
    semaphore.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué ricooooooooooooooooooooooo! Quedan {platosDisponibles} platos')
    if platosDisponibles <= 1:
      gateway.acquire()
     

Cocinero().start()

for i in range(5):
    gateway.release()
    logging.info(f'Quedan {platosDisponibles} platos')
    Comensal(i).start()

 # al correr el código se ejecuta  cocinero, rango, comenzal(0),rango, comensal(1)
 # rango, comensal(2), rango, rango ,cocinero  , comensal(3), cocinero, comensal(4)
 # cocinero, cocinero....... 
 # Logre cortar el bucle infinito, logre que no me arroje platos negativos,
 # pero no encuentro el error y no estoy conforme.

