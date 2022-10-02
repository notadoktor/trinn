def print_hex(data: bytes):
    print("".join("{:02x} ".format(x) for x in data))


def print_screen(data: bytes):
    SCREEN_H = 128
    SCREEN_W = 64

    scr = gen_screen(SCREEN_H + 1, SCREEN_W + 1)

    x = y = 0
    basey = 0

    for i in range(0, int(SCREEN_H * SCREEN_W / 8)):
        tmp = format(data[i], "b")
        tmp = tmp[::-1] + "0" * (8 - len(tmp))

        y = basey
        x += 1
        for c in tmp:
            scr[x][y] = c
            y += 1

        if (i + 1) % SCREEN_H == 0:
            basey += 8
            x = 0

    for y in range(0, SCREEN_W, 2):
        for x in range(1, SCREEN_H + 1):
            if scr[x][y] == " ":
                print(" ", end="")
                continue
            if int(scr[x][y]) == 1 and int(scr[x][y + 1]) == 1:
                print("\u2588", end="")
            if int(scr[x][y]) == 0 and int(scr[x][y + 1]) == 1:
                print("\u2584", end="")
            if int(scr[x][y]) == 1 and int(scr[x][y + 1]) == 0:
                print("\u2580", end="")
            if int(scr[x][y]) == 0 and int(scr[x][y + 1]) == 0:
                print(" ", end="")
        print()


def gen_screen(h: int, w: int, *, fill: str = "0"):
    return [["0" for col in range(w)] for row in range(h)]
