import pytest, numpy as np, random as rnd, math

def classifyTriangle(a, b, c):
    typ = 'None'
    if a == 0 or b == 0 or c == 0:
        return typ
    if a * b * c == a ** 3:
        typ = 'Equilateral'
    elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):
        typ = 'Isoceles'
    else:
        typ = 'Scalene'
    if a ** 2 + b ** 2 == round(c ** 2):
        typ += ' Right'
    return typ

if __name__ == '__main__':
    for i in range(3):
        a = rnd.randrange(1, 9, 1)
        b = rnd.randrange(1, 9, 1)
        c = rnd.randrange(1, 9, 1)
        print('Triangle with ', a, ',', b, ',', c, ' is ', classifyTriangle(a, b, c))
    a, b, c = 3, 3, 3 * math.sqrt(2)
    print('Triangle with ', a, ',', b, ',', c, ' is ', classifyTriangle(a, b, c))