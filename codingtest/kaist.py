# 깜짝퀴즈!!! s가 입구고 e가 탈출구 *가 보석 !가 벽일때 탈출하면서 최대로주울수있는 보석은 몇개일까요?
import copy

MAP_STR = '''s.!..*
..!...
..!...
..!*!*
......
*!....
**!!!e'''


def solution(map_str: str):
    map_arr = make_arr(map_str)
    return dfs(0, 0, map_arr, 0)


def print_map(map_arr):
    arr = []
    for row in map_arr:
        arr.append(''.join(row))
    print('')
    print('\n'.join(arr))
    print('')


def dfs(current_y, current_x, map_arr, score):
    # 도착
    if map_arr[current_y][current_x] == 'e':
        print_map(map_arr)
        return score

    # 보석 먹었으면 점수추가
    if map_arr[current_y][current_x] == '*':
        score += 1

    # 지나왔다고 표시
    map_arr[current_y][current_x] = 'X'

    max_answer = -1

    if current_y != 0 and map_arr[current_y - 1][current_x] != 'X' and map_arr[current_y - 1][current_x] != '!':
        answer = dfs(current_y - 1, current_x, copy.deepcopy(map_arr), score)
        max_answer = answer > max_answer and answer or max_answer

    if current_x != 0 and map_arr[current_y][current_x - 1] != 'X' and map_arr[current_y][current_x - 1] != '!':
        answer = dfs(current_y, current_x - 1, copy.deepcopy(map_arr), score)
        max_answer = answer > max_answer and answer or max_answer

    if current_y + 1 != len(map_arr) and map_arr[current_y + 1][current_x] != 'X' and map_arr[current_y + 1][current_x] != '!':
        answer = dfs(current_y + 1, current_x, copy.deepcopy(map_arr), score)
        max_answer = answer > max_answer and answer or max_answer

    if current_x + 1 != len(map_arr[current_y]) and map_arr[current_y][current_x + 1] != 'X' and map_arr[current_y][current_x + 1] != '!':
        answer = dfs(current_y, current_x + 1, copy.deepcopy(map_arr), score)
        max_answer = answer > max_answer and answer or max_answer

    return max_answer


def make_arr(map_str):
    rows = map_str.split('\n')
    return list(map(split_row, rows))


def split_row(row):
    return list(row)


print(solution(MAP_STR))
