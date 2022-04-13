class Deffi:

    def __init__(self):
        self.p = int(input("Введи p: "))
        self.g = int(input("Введи g: "))
        self.x = int(input("Введи x: "))
        self.y = int(input("Введи y: "))

    def find_a(self):
        return self.g**self.x % self.p

    def find_b(self):
        return self.g**self.y % self.p

    def find_ka(self):
        return Deffi.find_b(self)**self.x % self.p

    def find_kb(self):
        return Deffi.find_a(self)**self.y % self.p


d = Deffi()
print(f'A = {d.find_a()}')
print(f'B = {d.find_b()}')
print(f'k для абонента А = {d.find_ka()}')
print(f'k для абонента B = {d.find_kb()}')
