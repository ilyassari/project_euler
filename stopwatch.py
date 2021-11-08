import time

def stopwatch(func, *args, **kwargs):
    def inner(*arg, **kwargs):
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} süresi: {end_time - begin_time:0.4f} saniye")
        return result
    return inner
