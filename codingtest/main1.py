from datetime import datetime


def gen(num: int):
    for i in range(num):
        yield i


def gen2(num: int):
    ret = 0
    for i in range(num):
        ret += i
    return ret


def solution():
    num = 100000
    start_time = datetime.now()
    print(sum(gen(num)))
    end_time = datetime.now()
    print(end_time - start_time)
    start_time_2 = datetime.now()
    print(gen2(num))
    end_time_2 = datetime.now()
    print(end_time_2 - start_time_2)
    return 'end'


if __name__ == '__main__':
    print(solution())
