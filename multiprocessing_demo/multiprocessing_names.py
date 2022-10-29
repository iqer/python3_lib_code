import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(2)
    print(name, 'Exiting')


def my_service():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')


if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
    )

    worker_1 = multiprocessing.Process(
        name='worker_1',
        target=worker,
    )
    worker2 = multiprocessing.Process(
        name='worker_2',
        target=worker,
    )

    worker_1.start()
    worker2.start()
    service.start()
