def solution(name):
    change_cnt, move_cnt = move_and_change(name, 'A' * len(name), 0, 0)
    return change_cnt + move_cnt


def move_and_change(name, current, i, move_cnt):
    if name == current:
        return 0, 0

    change_cnt = change(name[i])
    current = list(current)
    current[i] = name[i]

    change_cnt_r, move_cnt_r = move_and_change(name, current, (i + 1) % len(name), move_cnt + 1)
    change_cnt_l, move_cnt_l = move_and_change(name, current, (i - 1) % len(name), move_cnt + 1)

    if move_cnt_r > move_cnt_l:
        return change_cnt + change_cnt_r, move_cnt_r
    return change_cnt + change_cnt_l, move_cnt_l


def change(char):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = 26
    index = alphabet.index(char)
    return index if index < length - index else length - index
