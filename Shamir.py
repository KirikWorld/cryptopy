p, x1, y1, X1 = int(input('p: ')), int(input('x1: ')), int(input('y1: ')), int(input('X1: '))
x2 = pow(x1, -1, p-1); y2 = pow(y1, -1, p-1)
print(f'x2 = {x2}, y2 = {y2}')
Y1 = pow(X1, y1, p); X2 = pow(Y1, x2, p)
print(f'Y1 = {Y1}, X2 = {X2}')
Y2 = pow(X2, y2, p)
print(f'Y2 = M = {Y2}')