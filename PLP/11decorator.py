from datetime import datetime


def timer(func):
    def wrapper():
        t1 = datetime.now()
        func()
        timer = datetime.now() - t1
        print timer
    return wrapper


@timer
def this_takes_long_time():
    a = []
    for i in range(1003300):
        a.append({'a': {'b': []}})


this_takes_long_time()
