import random
import math
from decimal import Decimal

min, max = 1000, 9999
simple_numbers = []
alphabet = {key: num for key, num in list(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', range(1, 34)))}
print(alphabet)

# простое ли число
def simple(value):
    d = 2
    while _ % d != 0:
        d += 1
    if d == _:
        return True
    else:
        return False


# простые числа в диапазоне от мин до мах
for _ in range(min, max):
    if simple(_) == True:
        simple_numbers.append(_)

p, q = random.choice(simple_numbers), random.choice(simple_numbers)  # находим p и q
n = p * q  # находим n
fi = (p - 1)*(q - 1)  # находим fi

# находим е, если е не взаимно простое с фи, то выбираем по новой
e = random.randint(1, 300)
while math.gcd(fi, e) != 1:
    e = random.randint(1, 300)

d = 1  # находим d
while math.fmod(p * d, fi) != 1:
    d += 1

print(f'Открытый ключ - (e: {e}, n: {n})')
print(f'Закрытый ключ - (d: {d}, n: {n})')


# шифруем
def encryption(alphabet, text='тест'):
    encrypt_message = []
    for _ in text:
        encrypt_message.append(math.fmod(Decimal(alphabet.get(_)**e), n))
    
    return encrypt_message

ala = encryption(alphabet)
print(ala)

# # дешифруем 
# def decryption(alphabet, text, d, n):
#     decrypt_message = []
#     for _ in text:
#         decrypt_message.append(math.fmod(Decimal(_)**Decimal(d), n))
        
#     decrypt_message = [alphabet[_] for _ in decrypt_message]
#     return decrypt_message

# print(decryption(alphabet, ala, d, n))
