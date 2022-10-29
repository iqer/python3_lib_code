import logging
import threading
import time


def wait_for_event(e):
    logging.debug('wait for event starting')
    event_is_set = e.wait()
    logging.debug(f'event set: {event_is_set}')


def wait_for_event_timeout(e, t):
    while not e.is_set():
        logging.debug('wait for event timeout starting')
        event_is_set = e.wait(t)
        logging.debug(f'event set: {event_is_set}')
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other worker')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()
t1 = threading.Thread(
    name='block',
    target=wait_for_event_timeout,
    args=(e, 2)
)

t1.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event,
    args=(e,),
)

t2.start()

logging.debug('waiting before calling event.set()')
time.sleep(4)
e.set()
logging.debug('Event is set')
