from random import *
import os


welcome_text = ('Приветствую Вас, на игре, \n'
                'Я даю Вам 2021 конфету, вы берете их по очереди,\n'
                'причем, за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
                'Ну что начнем?')
print(welcome_text)

message = ['твоя очередь']


def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = input('\nА твоего соперника?: ')

    print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
    print('\nДля начала опеределим кто первый начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky} ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Все кончились конфетки')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 0
        else:
            print('Баста, карапузик, кончились конфетки')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()


