class RSAHack:

    def __init__(self, N, e1, e2, c1, c2):
        self.N = N
        self.e1 = e1
        self.e2 = e2
        self.c1 = c1
        self.c2 = c2

    def r_and_s(self):
        if self.e1 > self.e2:
            midle_val = self.e1 % self.e2
        else:
            midle_val = self.e2 % self.e1
        self.r = midle_val
        self.s = midle_val
        while self.r * self.e1 + self.s * self.e2 != 1:
            if (self.r*self.e1 + self.s*self.e2 > 1):
                self.s -= 1
            if (self.r*self.e1 + self.s*self.e2 < 1):
                self.r += 1
        return self.r, self.s

    def find_M(self):
        RSAHack.r_and_s(self)
        return (pow(self.c1, self.r, self.N) * pow(self.c2, self.s, self.N) % self.N)


r = RSAHack(N=27641, e1=341, e2=391, c1=9006, c2=14547)
print('Пример №1:', r.find_M())

r = RSAHack(N=17819, e1=121, e2=125, c1=5051, c2=2841)
print('Пример №2:', r.find_M())

r = RSAHack(N=19939, e1=625, e2=527, c1=7537, c2=7851)
print('Пример №3:', r.find_M())

r = RSAHack(N=17201, e1=121, e2=325, c1=15151, c2=11134)
print('Пример №4:', r.find_M())

r = RSAHack(N=26797, e1=169, e2=187, c1=20412, c2=12342)
print('Пример №5:', r.find_M())
