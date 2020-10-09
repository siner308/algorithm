def solution(remain_count, input_string):
    if not remain_count:
        return input_string

    answer = ''
    length = len(input_string)
    cnt = 0
    target = ''
    for i in range(length):
        if cnt == 0:  # 새로운 문자열
            target = input_string[i]
        if input_string[i] != target:  # 다른 숫자가 들어옴
            answer += '%s%s' % (cnt, target)
            cnt = 0
        elif input_string[i] == target:  # 계속해서 같은 문자열이 들어옴
            cnt += 1
    answer += '%s%s' % (cnt, target)
    return solution(remain_count - 1, answer)


if __name__ == '__main__':
    answer = solution(5, '1')
    print(answer)
