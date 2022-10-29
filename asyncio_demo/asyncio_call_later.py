import asyncio


def callback(n):
    print(f'callback {n} invoked')


async def main(loop):
    print('registering callbacks')
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)


event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)

try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
