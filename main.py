import time

def decorator_countdown(function):
    def wrapper():
        return function()
    return wrapper


@decorator_countdown
def countdown():
    n = int(input("Seconds : "))
    while n > 0:
        time.sleep(1)
        yield n
        n -= 1

for i in countdown():
     print(i)
