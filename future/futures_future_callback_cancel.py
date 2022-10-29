from concurrent import futures
import time


def task(n):
    print(f'{n}: sleeping')
    time.sleep(0.5)
    print(f'{n}: done')
    return n / 10


def done(fn):
    if fn.cancel():
        print(f'{fn.arg} cancel')
    elif fn.done():
        print(f'{fn.arg}: not cancel')


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    tasks = []
    for i in range(10, 0, -1):
        print(f'main: submitting {i}')
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))

    for i, t in reversed(tasks):
        if not t.cancel():
            print(f'main: did not cancel {i}')

    ex.shutdown()