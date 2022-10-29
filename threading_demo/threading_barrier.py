import threading
import time


def worker(barrier):
    print(
        f'{threading.current_thread().name} waiting for barrier with {barrier.n_waiting} others')
    worker_id = barrier.wait()
    print(f'{threading.current_thread().name} after barrier {worker_id}')


NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS)

threads = [
    threading.Thread(
        name=f'worker-{i}',
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(f'{t.name} starting')
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()
