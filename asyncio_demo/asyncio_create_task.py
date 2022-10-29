import asyncio


async def task_func():
    print('in task func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print(f'waiting for {task}')
    return_value = await task
    print(f'task completed {task}')
    print(f'return value {return_value}')


event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)

try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
