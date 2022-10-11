import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
st_letters = 'il1Lo0O'


chars  = ''

def inspection_answer():
    global inp
    inp = input('Введите y - ДА, n - НЕТ\n')
    if inp != 'y' and inp != 'n':
        print(qwestion)
        inspection_answer()


def generate_password(length, chars):

    for _ in range(length_of_pass):
        pas = random.sample(chars, length_of_pass)
        return ('').join(pas)

# Вопросы пользователю про пароль
number_of_pass = int(input('Введите кличество паролей, которое вы хотите сгенерировать\n'))

length_of_pass = int(input('Введите число символов из которых должен состоять каждый пароль\n'))


qwestion = 'Использовать в пароле цифры 0123456789?'
print(qwestion)
inspection_answer()
if inp == 'y':
    chars += digits


qwestion = 'Использовать в пароле прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
print(qwestion)
inspection_answer()
if inp == 'y':
    chars += uppercase_letters


qwestion = 'Использовать в пароле строчные буквы abcdefghijklmnopqrstuvwxyz?'
print(qwestion)
inspection_answer()
if inp == 'y':
    chars += lowercase_letters


qwestion = 'Использовать в пароле символы !#$%&*+-=?@^_?'
print(qwestion)
inspection_answer()
if inp == 'y':
    chars += punctuation

chars = list(chars)

if len(chars) > 0:
    qwestion = 'Исключить в пароле символы il1Lo0O'
    print(qwestion)
    inspection_answer()
    if inp == 'y':
        st_letters = list(st_letters)
        for i in st_letters:
            if i in chars:
                chars.remove(i)

for _ in range(number_of_pass):
    print(generate_password(number_of_pass, chars))