from concurrent import futures
import os
import signal

with futures.ThreadPoolExecutor(max_workers=2) as ex:
    print('getting the pid for one worker')
    f1 = ex.submit(os.getpid)
    pid1 = f1.result()

    print(f'killing process {pid1}')
    os.kill(pid1, signal.SIGHUP)
    print('submitting another task')
    f2 = ex.submit(os.getpid)

    try:
        pid2 = f2.result()
    except futures.process.BrokenProcessPool as e:
        print(f'could not start new tasks: {e}')
