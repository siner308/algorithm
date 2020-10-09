import random
from datetime import datetime


def times_with_numba(ans, num):
    return ans * num


def times_without_numba(ans, num):
    return ans * num


def func_with_numba(num: int):
    ans = 1
    for i in range(num):
        ans = times_with_numba(ans, i)
    return ans


def func_without_numba(num: int):
    ans = 1
    for i in range(num):
        ans = times_with_numba(ans, i)
    return ans


def solution():
    start_time = datetime.now()
    func_with_numba(10000000)
    end_time = datetime.now()
    print(end_time - start_time)
    start_time = datetime.now()
    func_without_numba(10000000)
    end_time = datetime.now()
    print(end_time - start_time)
    answer = 5
    return answer


if __name__ == '__main__':
    print(solution())
