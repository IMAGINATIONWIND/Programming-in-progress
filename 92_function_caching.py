from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fn(x):
    time.sleep(3)
    return x*5

print(fn(1))
print("COMPLETED")
print(fn(2))
print("COMPLETED")
print(fn(3))
print("COMPLETED")
print(fn(1))
print("COMPLETED")
print(fn(2))
print("COMPLETED")