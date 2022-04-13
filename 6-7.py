def findC(N1, e1, N2, e2, M):
    a = int(input('Введите абонента получателя '))
    if a == 1:
        C = pow(M, e1, N1)
        print('C = %d'%C)
    elif a == 2:
        C = pow(M, e2, N2)
        print('C = %d'%C)
    else:
        print('Ошибка')

findC(989, 25, 899, 121, 150)



def find_d(N1, e1, N2, e2, C, p, q):
    a = int(input('Введите абонента получателя '))
    if a == 1:
        D = pow(e1, -1, (p-1)*(q-1))
        M = pow(C, D, N1)
        print('D = %d'%D, 'M = %d'%M)
    elif a == 2:
        D = pow(e2, -1, (p-1)*(q-1))
        M = pow(C, D, N2)
        print('D = %d'%D, 'M = %d'%M)
    else:
        print('Ошибка')

find_d(899, 121, 989, 25, 744, 23, 42)
find_d(989, 25, 899, 121, 584, 31, 29)