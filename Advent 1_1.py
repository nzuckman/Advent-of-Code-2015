def instr(n):
    n = list(str(n))
    floor = 0
    for inst in n:
        if inst == '(':
            floor += 1
        if inst == ')':
            floor -= 1
    return floor
