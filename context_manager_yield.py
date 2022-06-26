from contextlib import contextmanager
import time


@contextmanager
def timer():
    start_time = time.time()
    yield
    res = time.time() - start_time
    print(f"— %s seconds —  {res}")


with timer():
    for i in range(10):
        junk = list(range(i**2))
        print("–DONE–")