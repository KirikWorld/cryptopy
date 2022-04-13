import random


class Gamal:
    alphabet = list(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюя ', range(1, 35)))
    alphabet = {x: y for x, y in alphabet}

    def __init__(self):
        self.msg = str(input('Введите сообщение: ')).lower()
        self.num_alphabet = [self.alphabet[_] for _ in self.msg]

    def simple(value):
        d = 2
        while value % d != 0:
            d += 1
        if d == value:
            return True
        else:
            return False

    def keygen(self):
        self.p = random.randint(37, 251)
        while not Gamal.simple(self.p):
            self.p = random.randint(3, 110)
        self.x = random.randint(2, self.p-1)

        def g_generate(self):
            d_list = [_ for _ in range(2, self.p-1) if (self.p-1) % _ == 0]
            if self.p == 2:
                return 1
            elif self.p == 5:
                return 7
            self.value = 2

            def proizvod(self):
                passed = 0
                for _ in range(len(d_list)):  # первопроизводный корень
                    if (self.value**d_list[_]-1) % self.p != 0:
                        passed += 1
                    else:
                        passed -= 1

                if passed != len(d_list):
                    self.value += 1
                    proizvod(self)

                return self.value
            return proizvod(self)

        self.y = pow(g_generate(self), self.x, self.p)

        return {'p': self.p, 'g': g_generate(self), 'x': self.x, 'y': self.y}

    def encrypt(self):
        encrypt_msg = []
        keys = Gamal.keygen(self)
        session_key = random.randint(2, keys['p']-1)  # = k
        a = pow(keys['g'], session_key, keys['p'])
        for M in self.num_alphabet:
            b = (keys['y']**session_key * M) % keys['p']
            encrypt_msg.append((a, b))

        print(f'{keys}\nСессионный ключ: {session_key}')
        print(f'Зашифрованное сообщение: {encrypt_msg}')
        return encrypt_msg, self.x


g = Gamal()
msg = g.encrypt()


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def decrypt(encrypt_msg, x):
    decrypt_msg = []
    finish_answer = []
    for _ in encrypt_msg:
        decrypt_msg.append((_[1]*_[0]**(g.p-1-x)) % g.p)
    for _ in decrypt_msg:
        finish_answer.append(get_key(g.alphabet, _))
    return finish_answer


lal = decrypt(msg[0], msg[1])
print("".join(lal))
