import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print(f'Starting: {p.name}, {p.pid}')
    sys.stdout.flush()
    time.sleep(2)
    print(f'Exiting: ', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print(f'Starting: {p.name}, {p.pid}')
    sys.stdout.flush()
    print(f'Exiting: {p.name}, {p.pid}')
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
    )

    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )

    d.start()
    time.sleep(1)
    n.start()

    d.join(1)
    print(d.is_alive())

