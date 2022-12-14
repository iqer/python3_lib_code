import logging
import threading
import time


def consumer(cond):
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')


def producer(cond):
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making Resource available')
        cond.notify_all()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

condition = threading.Condition()

c1 = threading.Thread(target=consumer, args=(condition,))
c2 = threading.Thread(target=consumer, args=(condition,))

p = threading.Thread(name='p', target=producer, args=(condition,))
c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()
