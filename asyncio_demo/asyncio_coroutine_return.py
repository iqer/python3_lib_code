import asyncio


async def coroutine():
    print('in coroutine')
    return 'result'


event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)


try:
    return_value = event_loop.run_until_complete(
        coroutine()
    )
    print(f'it returned: {return_value}')
finally:
    event_loop.close()