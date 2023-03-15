from time import time, sleep

def do_log(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func
        result()
        print(result.__name__, "time =", time() - start_time)
        return result
    return wrapper

@do_log
def MySUPERfunc():
    sleep(3)
    print("Hi")

MySUPERfunc()
