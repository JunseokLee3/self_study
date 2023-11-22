n, m, k = tuple(map(int, input().split()))

board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    board[i] = [0] + list(map(int, input().split()))

next_board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

traveler = [(-1, -1)] + [
    tuple(map(int, input().split()))
    for _ in range(m)
]

exits = tuple(map(int, input().split()))

ans = 0

sx, sy, square_size = 0, 0, 0


def move_all_traveler():
    global exits, ans

    for i in range(1, m + 1):
        if traveler[i] == exits:
            continue

        tx, ty = traveler[i]
        ex, ey = exits

        if tx != ex:
            nx, ny  = tx, ty

            if ex > nx:
                nx += 1
            else:
                nx -= 1
                

for _ in range(k):
    move_all_traveler()

    is_all_escaped = True

    for i in range(1, m + 1):
        if traveler[i] != exits:
            is_all_escaped = False

    if is_all_escaped:
        break

    find_minimum_square()

    rotate_square()

    rotate_traveler_and_exit()

print(ans)