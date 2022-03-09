import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time()

        print("Total time", finish-start)
    return wrapper

def counter():
    time.sleep(3)

counter = calculate_time(counter)
counter()