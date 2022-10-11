import random
from random import *

def is_valid(num):
    try:
        if 1<= int(num) <= p:
            return True
        else:
            return False
    except ValueError:
        return False

def compare(num):
    if num < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        return False
    elif num > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        return False
    else:
        print(f'Вы угадали c {attemp} попытки, поздравляем!')
        return True

def attemp():
    global attemp
    attemp = 0

def generator():
    global n
    n = randint(1, p)

def game_over():
    print('y - сыграть еще раз, n - мне уже достаточно')
    global select
    select = input().lower()
    if select != 'y' and select != 'n':
        game_over()


attemp()

print('Добро пожаловать в числовую угадайку')


while True:
    if attemp == 0:
        print(f'Введите целое число N, что бы задать диапазон случайного числа от 1 до N')
        p = int(input())
        generator()

    print(f'Введите целое число от 1 до {p}')
    input_num = input()
    attemp +=1
    if not is_valid(input_num):
        print(f'А может быть все-таки введем целое число от 1 до {p}?')
        continue
    else:
        input_num = int(input_num)
        if not compare(input_num):
            continue
        else:
            print('Хотите сыграть еще раз?')
            game_over()
            if select == 'y':
                attemp = 0
                continue
            else:
                break



        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')