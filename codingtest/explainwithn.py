def solution(N, number):
    return calc(N, number)


def calc(N, number):
    # 잘못된 계산
    if number < 0:
        return -1
    elif number - N == 0:
        return 1
    elif int(number / N) == 0:
        return 1
    elif number - 1 == 0:
        return 2
    elif number - 11 == 0:
        return 3
    elif number - 111 == 0:
        return 4
    elif number - 1111 == 0:
        return 5
    elif number - 11111 == 0:
        return 6

    cases = []
    calc1 = calc(N, number - N)
    if calc1 >= 0:
        cases.append(calc1)
    calc2 = calc(N, int(number / N))
    if calc2 >= 0:
        cases.append(calc2)
    calc3 = calc(N, number - 1)
    if calc3 >= 0:
        cases.append(calc3)
    calc4 = calc(N, number - 11)
    if calc4 >= 0:
        cases.append(calc4)
    calc5 = calc(N, number - 111)
    if calc5 >= 0:
        cases.append(calc5)
    calc6 = calc(N, number - 1111)
    if calc6 >= 0:
        cases.append(calc6)
    calc7 = calc(N, number - 11111)
    if calc7 >= 0:
        cases.append(calc7)
    ret = 9999999
    for case in cases:
        if case < ret:
            ret = case
    return ret
