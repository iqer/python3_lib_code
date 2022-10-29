import multiprocessing


def producer(ns, event):
    ns.value = 'this is the value'
    event.set()


def consumer(ns, event):
    try:
        print(f'Before event: {ns.value}')
    except Exception as err:
        print(f'Before event, error: {str(err)}')
    event.wait()
    print(f'After event: ', ns.value)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()

    p = multiprocessing.Process(
        target=producer,
        args=(namespace, event,),
    )
    c = multiprocessing.Process(
        target=consumer,
        args=(namespace, event),
    )
    c.start()

    p.start()

    c.join()
    p.join()
