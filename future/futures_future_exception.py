from concurrent import futures


def task(n):
    print(f'{n} starting')

    raise ValueError(f'the value {n} is not good')


ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)

error = f.exception()
print(f'main: error: {error}')

try:
    result = f.result()
except ValueError as e:
    print(f'main: saw error {e} when accessing result')
