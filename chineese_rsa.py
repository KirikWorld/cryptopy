class Chineese:

    def __init__(self, N1, N2, N3, e, C1, C2, C3):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
        self.e = e
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        
    def find_y(self):
        self.Y = self.N1 * self.N2 * self.N3
        return self.Y
    
    def find_all_y(self):
        self.y1 = self.N2 * self.N3
        self.y2 = self.N1 * self.N3
        self.y3 = self.N1 * self.N2
        return self.y1, self.y2, self.y3
    
    def find_all_n(self):
        self.n1 = pow(self.y1, -1, self.N1)
        self.n2 = pow(self.y2, -1, self.N2)
        self.n3 = pow(self.y3, -1, self.N3)
        return self.n1, self.n2, self.n3
    
    def find_s(self):
        self.S = self.C1 * self.n1 * self.y1 + self.C2 * self.n2 * self.y2 + self.C3 * self.n3 * self.y3
        return self.S
    
    def find_c(self):
        self.C = pow(self.S, 1, self.Y)
        return self.C
    
    def find_m(self):
        self.M = round(pow(self.C, 1/3))
        return self.M
    

c = Chineese(N1=407, N2=391, N3=377, e=3, C1=51, C2=271, C3=213)
print("Y =", c.find_y())
print("y1, y2, y3 =", c.find_all_y())
print("n1, n2, n3 =", c.find_all_n())
print("S =", c.find_s())
print("C =", c.find_c())
print("M =", c.find_m(), end='\n\n')

c = Chineese(N1=403, N2=493, N3=437, e=3, C1=402, C2=378, C3=343)
print("Y =", c.find_y())
print("y1, y2, y3 =", c.find_all_y())
print("n1, n2, n3 =", c.find_all_n())
print("S =", c.find_s())
print("C =", c.find_c())
print("M =", c.find_m(), end='\n\n')

c = Chineese(N1=589, N2=481, N3=667, e=3, C1=388, C2=27, C3=635)
print("Y =", c.find_y())
print("y1, y2, y3 =", c.find_all_y())
print("n1, n2, n3 =", c.find_all_n())
print("S =", c.find_s())
print("C =", c.find_c())
print("M =", c.find_m(), end='\n\n')

c = Chineese(N1=703, N2=713, N3=493, e=3, C1=563, C2=140, C3=89)
print("Y =", c.find_y())
print("y1, y2, y3 =", c.find_all_y())
print("n1, n2, n3 =", c.find_all_n())
print("S =", c.find_s())
print("C =", c.find_c())
print("M =", c.find_m(), end='\n\n')

c = Chineese(N1=527, N2=551, N3=851, e=3, C1=281, C2=486, C3=75)
print("Y =", c.find_y())
print("y1, y2, y3 =", c.find_all_y())
print("n1, n2, n3 =", c.find_all_n())
print("S =", c.find_s())
print("C =", c.find_c())
print("M =", c.find_m(), end='\n\n')
