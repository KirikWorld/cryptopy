class Gamal:
    
    def encrypt(self):
        encrypt_msg = None
        inp_p = 23
        inp_g = 10
        inp_y = 13
        inp_M = 10
        inp_k = 2
        keys = inp_p, inp_g, inp_y
        session_key = inp_k  # = k
        a = pow(inp_g, session_key, inp_p)
        b = (inp_y**session_key * inp_M) % inp_p
        encrypt_msg = (a, b)

        print(f'{keys}\nСессионный ключ: {session_key}')
        print(f'Зашифрованное сообщение: {encrypt_msg}')
        return encrypt_msg
    
    
    def decrypt(self):
        inp_p = 11
        inp_g = 10
        
        """
        хз зачем эта переменная (g), если она не используется (пример с сайта https://swsu.ru/sveden/files/
        MU_PZ_Informacionnaya_bezopasnosty_No_4_Ely-Gamalya_-_kopiya.pdf?ysclid=l1wjxd2agw)
        """
        
        inp_x = 8
        inp_r = 6
        inp_s = 9
        finish_answer = None
        
        finish_answer = ((inp_s*inp_r**(inp_p-1-inp_x)) % inp_p)
        return f"M = {finish_answer}"


g = Gamal()
msg = g.encrypt()
print(g.decrypt())