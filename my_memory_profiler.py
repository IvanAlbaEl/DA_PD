import os
import psutil

# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

# decorator function
def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        mem_diff_gb = (mem_after - mem_before) / (1024 ** 3)
        print("{}: consumed memory: {:.6f} GB".format(
            func.__name__,
            mem_diff_gb
        ))
        return result
    return wrapper


