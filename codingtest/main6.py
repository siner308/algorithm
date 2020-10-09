import random
from datetime import datetime
from typing import List


def check(num):
    if num % 2 == 0:
        pass
    else:
        return num


def mapppp(nums):
    return map(lambda x: x * x, nums)


def forrrr(nums):
    for i, index in enumerate(nums):
        nums[i] *= nums[i]
    return nums


def solution():
    nums = [x for x in range(1000)]

    start_time = datetime.now()
    nums_for = forrrr(nums.copy())
    end_time = datetime.now()
    print(end_time - start_time)
    # print(nums_for)

    start_time = datetime.now()
    nums_map = mapppp(nums.copy())
    end_time = datetime.now()
    print(end_time - start_time)
    print(nums_map)
    # for _ in nums_map:
    #     print(_)

    # length = len(set(nums_for) & set(nums_map))
    # if length == len(nums_for) and length == len(nums_map):
    #     return 'same!!'
    answer = 5
    return answer


if __name__ == '__main__':
    print(solution())
