import threading


lock = threading.RLock()

print(f'first try: {lock.acquire()}')
print(f'second try: {lock.acquire()}')
