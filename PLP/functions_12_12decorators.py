from datetime import datetime, timedelta
from functools import wraps


def timeit(func):

    @wraps(func)
    def wrapper():
        t1 = datetime.now()
        func()
        timeit._total_time += datetime.now() - t1
    return wrapper


timeit._total_time = timedelta(0)


@timeit
def this_takes_long_time():
    a = []
    for i in range(1003300):
        a.append({'a': {'b': []}})

@timeit
def gogu():
    a = []
    for i in range(1003300):
        a.append({'a': {'b': []}})


this_takes_long_time()
this_takes_long_time()
this_takes_long_time()
gogu()

print timeit._total_time
