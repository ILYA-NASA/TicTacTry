

def start_of_tic_tac_toe_game():
    import random
    mark = input('Вы будете играть крестиками (X) или ноликами (O)? ')
    mark = mark.upper()
    bot = bool(input('Вы будете играть c ботом? (1 - да,0 - нет) '))
    
    if mark != 'X' or 'O':
    # mark = input('Вы ввели не те знаки. Выберите х или о: ')  если хотим, чтобы все же пользователь ввел правильные данные
    # mark = mark.upper()
        mark = ['X', 'O']       # если хотим быстрее началь играть :)
        mark = random.choice(mark)
        print(f'Вы ввели не то, поэтому выбор сделан за вас. Вы играете за {mark}')
    
    return mark,bot

