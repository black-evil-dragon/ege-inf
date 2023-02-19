from functools import lru_cache

limit = 88
x = 6


@lru_cache(None)
def f(x, y):
    if x + y >= limit: return 0

    moves = [
        f(x + 1, y), f(x, y + 1),
        f(x * 3, y), f(x, y * 3),
    ]

    lose = [
        i for i in moves if i <= 0
    ]

    if lose:
        return -max(lose) + 1
    else:
        return -max(moves)

n1 = []
n2 = []
n3 = []

for s in range(1, limit):
    result = f(x, s)
    print(s, result)

    if result == 1:
        n1.append(f'{s, result}')
    elif result == 2:
        n2.append(f'{s, result}')
    elif result == -1:
        n3.append(f'{s, result}')

print(
    f'1--{int(n1[0][1] + n1[0][2]) / 3}\n{n2}\n{n3}'
)




















