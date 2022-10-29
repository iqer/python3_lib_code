import asyncio
import functools


def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def coco1(lock):
    print('coro1 waiting for the lock')
    with await lock:
        print('coco1 acquired lock')
    print('coco1 released lock')


async def coco2(lock):
    print('coco2 waiting for the lock')
    await lock
    try:
        print('coco2 acquired lock')
    finally:
        print('coco2 released lock')
        lock.release()


async def main(loop):
    lock = asyncio.Lock()
    print('acquiring the lock before starting coroutines')
    await lock.acquire()
    print(f'lock acquired: {lock.locked()}')
    loop.call_later(0.1, functools.partial(unlock, lock))

    print('waiting for coroutines')
    await asyncio.wait([coco1(lock), coco2(lock)])


event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)


try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()