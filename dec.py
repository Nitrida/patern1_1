import functools
import time

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} выполнеие {runtime:.4f} сек")
        return result
    return _wrapper

@timer
def complex_calculation():
    a =15
    time.sleep(0.5)
    return a

print(complex_calculation())