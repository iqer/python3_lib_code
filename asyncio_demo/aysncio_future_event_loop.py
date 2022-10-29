import asyncio


def mark_done(future, result):
    print(f'setting future result to {result}')
    future.set_result(result)


event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)

try:
    all_done = asyncio.Future()
    print('scheduling mark_done')
    event_loop.call_soon(mark_done, all_done, 'the result')

    print('entering event loop')
    result = event_loop.run_until_complete(all_done)
    print(f'returned result: {result}')
finally:
    print('closing event loop')
    event_loop.close()

print(f'future result: {all_done.result()}')
