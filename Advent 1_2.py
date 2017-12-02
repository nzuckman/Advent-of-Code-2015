def instr(n):
    n = list(str(n))
    pla = 0
    floor = 0
    for inst in n:
        if inst == '(':
            floor += 1
            pla += 1
        if inst == ')':
            floor -= 1
            pla += 1
            if floor == -1:
                return pla
    return
