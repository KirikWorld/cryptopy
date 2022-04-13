class Chinese_solve:
    def __init__(self, x1, mod1, x2, mod2, x3, mod3):
        self.x1 = x1
        self.mod1 = mod1
        self.x2 = x2
        self.mod2 = mod2
        self.x3 = x3
        self.mod3 = mod3

    def get_M(self):
        return self.mod1 * self.mod2 * self.mod3

    def get_allM(self, M):
        return M // self.mod1, M // self.mod2, M // self.mod3

    def get_allY(self, allM):
        return pow(allM[0], -1, self.mod1), pow(allM[1], -1, self.mod2), pow(allM[2], -1, self.mod3)

    def solve(self, M, allM, allY):
        return pow(self.x1 * allM[0] * allY[0] + self.x2 * allM[1] * allY[1] + self.x3 * allM[2] * allY[2], 1, M)


C = Chinese_solve(5, 7, 3, 11, 10, 13)

M = C.get_M()
allM = C.get_allM(M)
allY = C.get_allY(allM)

print(C.solve(M, allM, allY))