from datetime import datetime


def po(arr):
    print(datetime.now())
    for i in range(len(arr)):
        arr.pop(0)
    print(datetime.now())


def remo(arr):
    print(datetime.now())
    for i in range(len(arr)):
        arr.remove(arr[i])
    print(datetime.now())


po([1] * 100000)
try:
    remo([1] * 100000)
except:
    print(datetime.now())

