import multiprocessing
import os


def do_calculation(data):
    return data * 2


def start_process():
    print(f'Starting {multiprocessing.current_process().name}')


if __name__ == '__main__':
    inputs = list(range(10))
    print(f'input: {inputs}')

    builtin_outputs = list(map(do_calculation, inputs))
    print(f'builtin: {builtin_outputs}')

    pool_size = os.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
    )

    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()
    print(f'Pool: {pool_outputs}')
