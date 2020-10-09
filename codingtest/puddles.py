def solution(m, n, puddles):
    puddles = sorted(puddles, key=(lambda l: (l[0], l[1])))
    ways = [[None for i in range(m)] for j in range(n)]
    for row, y in zip(ways, range(len(ways))):
        for col, x in zip(row, range((len(ways[0])))):
            if y == 0 or x == 0:
                ways[y][x] = 1
                print(y, x)
            else:
                ways[y][x] = ways[y - 1][x] + ways[y][x - 1]
    for puddle, idx in zip(puddles, range(len(puddles))):
        ways[puddle[0] - 1][puddle[1] - 1] = 0
    for y in range(n):
        for x in range(m):
            if x == 0 or y == 0:
                continue
            elif ways[y][x] != 0:
                ways[y][x] = ways[y - 1][x] + ways[y][x - 1]
    print(ways)

    return ways[n - 1][m - 1]


if __name__ == '__main__':
    answer = solution(4, 3, [[2, 2]])
    print(answer)

