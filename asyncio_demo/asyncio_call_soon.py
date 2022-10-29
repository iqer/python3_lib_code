import asyncio
import functools


def callback(arg, *, kwargs='default'):
    print(f'callback invoked with {arg} and {kwargs}')


async def main(loop):
    print('registering callbacks')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwargs='not default')
    loop.call_soon(wrapped, 2)

    await asyncio.sleep(10)


event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)

try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
