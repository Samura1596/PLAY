import time

# Определяем стартовую комнату
current_room = 'start'

# Определяем инвентарь игрока
inventory = []

# Функция для отображения описания комнаты
def show_room():
    global current_room

    # Отображаем описание текущей комнаты
    if current_room == 'start':
        print('Вы находитесь в заброшенной библиотеке. Справа от вас находится дверь, а слева от вас — стеллаж.')
    elif current_room == 'shelf':
        print('Вы находитесь у стеллажа с книгами. Вам ничего неинтересно находится на верхних полках, но снизу вы замечаете книгу, которая блистит под странным углом.')
    elif current_room == 'door':
        print('Вы стоите у двери. Она заперта, но вы замечаете ключ рядом на полу.')
    elif current_room == 'corridor':
        print('Вы прошли через дверь и теперь находитесь в коридоре. Возможно, стоит поторопиться, вы чувствуете, что вас преследуют.')
    elif current_room == 'monster':
        print('Вы обнаружили злобного монстра! Вы должны сразить его, чтобы продолжить свой путь к магу!')
    elif current_room == 'mage':
        print('Вы добрались до кабинета мага. Вы должны победить его, чтобы освободить замок, и выбраться из этого места!')

# Функция для обработки действий игрока
def handle_action():
    global current_room, inventory

    # Получаем команду от игрока
    action = input('Что бы вы хотели сделать? ')

    # Обрабатываем команду
    if current_room == 'start':
        if action == 'пойти к стеллажу':
            current_room = 'shelf'
        elif action == 'пойти к двери':
            current_room = 'door'
        else:
            print('Неизвестная команда!')
    elif current_room == 'shelf':
        if action == 'поднять книгу':
            inventory.append('ключ')
            print('Вы подняли ключ.')
        elif action == 'пойти обратно':
            current_room = 'start'
        else:
            print('Неизвестная команда!')
    elif current_room == 'door':
        if action == 'поднять ключ':
            inventory.append('ключ')
            print('Вы подняли ключ.')
        elif action == 'открыть дверь':
            if 'ключ' in inventory:
                current_room = 'corridor'
                print('Вы открыли дверь и прошли в коридор.')
            else:
                print('Дверь заперта. Вам нужен ключ.')
        else:
            print('Неизвестная команда!')
    elif current_room == 'corridor':
        if action == 'пройти дальше':
            current_room = 'monster'
            print('Вы прошли дальше и обнаружили злобного монстра!')
        else:
            print('Неизвестная команда!')
    elif current_room == 'monster':
        if action == 'сражаться':
            print('Вы сражаетесь с монстром...')
            time.sleep(2)
            print('Ура! Вы победили монстра!')
            current_room = 'mage'
        else:
            print('Неизвестная команда!')
    elif current_room == 'mage':
        if action == 'сражаться':
            print('Вы сражаетесь с магом...')
            time.sleep(2)
            print('Ура! Вы победили мага!')
            print('Вы освободили замок и выбрались из этого места!')
            exit()
        else:
            print('Неизвестная команда!')

# Основной игровой цикл
while True:
    # Отображаем описание комнаты
    show_room()

    # Отображаем инвентарь игрока
    if inventory:
        print('Ваш инвентарь: {}'.format(', '.join(inventory)))

    # Обрабатываем действия игрока
    handle_action()