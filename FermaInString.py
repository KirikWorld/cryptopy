import math

def decision(N):
    t1 = math.ceil(math.sqrt(N))
    while math.sqrt((t1**2) - N) % 1 != 0: t1 += 1; p, q = int(t1) + int(math.sqrt((t1**2) - N)), int(t1) - int(math.sqrt((t1**2) - N)); print(f'p * q = {p * q} = N')
    return p, q
    
print('p, q =', decision(2183), end='\n\n')
print('p, q =', decision(5429), end='\n\n')
print('p, q =', decision(1891), end='\n\n')
print('p, q =', decision(7171), end='\n\n')
print('p, q =', decision(5723))
