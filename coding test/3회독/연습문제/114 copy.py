def solution(code):
    ret = ""
    mode = 0

    for idx, char in enumerate(code):
        if char == "1":
            mode = 1 - mode
        else:
            if mode == 0 and idx % 2 == 0:
                ret += char
            elif mode == 1 and idx % 2 != 0:
                ret += char

    for idx, char in enumerate(code):
        if char == "1":
            mode = 1 - mode
        else:
            if mode == 0 and idx % 2 == 0:
                ret += char
            elif mode == 1 and idx % 2 != 0:
                ret += char
    
    return ret if ret else "EMPTY"


def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"