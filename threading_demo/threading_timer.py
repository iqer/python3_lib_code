import threading
import time
import logging


def delayed():
    logging.debug('worker running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

t1 = threading.Timer(0.3, delayed)
t2 = threading.Timer(0.3, delayed)
t2.name = 't2'


logging.debug('starting timers')
t1.start()
t2.start()

time.sleep(0.2)
logging.debug(f'canceling {t2.name}')
t2.cancel()
logging.debug('done')

