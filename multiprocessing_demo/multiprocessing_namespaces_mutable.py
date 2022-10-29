import multiprocessing


def producer(ns, event):
    ns.my_list.append('this is the value')
    event.set()


def consumer(ns, event):
    print(f'before event: {ns.my_list}')
    event.wait()
    print(f'after event: {ns.my_list}')


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()
    namespace.my_list = []
    p = multiprocessing.Process(
        target=producer,
        args=(namespace, event),
    )
    c = multiprocessing.Process(
        target=consumer,
        args=(namespace, event),
    )

    c.start()
    p.start()

    c.join()
    p.join()
