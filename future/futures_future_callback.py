from concurrent import futures
import time


def task(n):
    print(f'{n}: sleeping')
    time.sleep(0.5)
    print(f'{n}: done')

    return n / 10


def done(fn):
    if fn.cancelled():
        print(f'{fn.arg}: cancelled')
    elif fn.done():
        error = fn.exception()
        if error:
            print(f'{fn.arg}: error returned: {error}')
        else:
            result = fn.result()
            print(f'{fn.arg}: value returned: {result}')


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    f = ex.submit(task, 5)
    f.arg = 5
    f.add_done_callback(done)
    result = f.result()
