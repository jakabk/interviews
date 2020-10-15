# Implement a context manager that measures the performance of the nested block and will print it out to the console.
# Example:
# >>> with performance:
# >>>     time.sleep(1.5)
# >>>
# 1.5000023
import time
from contextlib import contextmanager


@contextmanager
def performance():
    try:
        start = time.time()
        yield
    finally:
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    with performance() as perform:
        time.sleep(1.5)
