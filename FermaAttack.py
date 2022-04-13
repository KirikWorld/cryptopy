import math


class FermaAttack:

    def __init__(self, N):
        self.N = N

    def decision(self):
        t1 = math.ceil(math.sqrt(self.N))
        while math.sqrt((t1**2) - self.N) % 1 != 0:
            t1 += 1
        p, q = int(t1) + int(math.sqrt((t1**2) - self.N)
                             ), int(t1) - int(math.sqrt((t1**2) - self.N))
        print(f'p * q = {p * q} = N')
        return p, q


f = FermaAttack(2183)
print('p, q =', f.decision(), end='\n\n')

f = FermaAttack(5429)
print('p, q =', f.decision(), end='\n\n')

f = FermaAttack(1891)
print('p, q =', f.decision(), end='\n\n')

f = FermaAttack(7171)
print('p, q =', f.decision(), end='\n\n')

f = FermaAttack(5723)
print('p, q =', f.decision())
