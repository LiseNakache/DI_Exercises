import time

def timeMe(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        duration = end-start
        print("Time: ", duration)
        
    return wrapper

@timeMe
def count(n):
    for i in range(n+1):
        print(i)


@timeMe
def printName(name):
    print(name)


count(100)
