

def start_of_tic_tac_toe_game():
    import random
    mark = input('Вы будете играть крестиками (X) или ноликами (O)? ')
    mark = mark.upper()
    
    while True:
        if mark == 'X':
            return True
        if mark == 'O':
            return False
        # mark = input('Вы ввели не те знаки. Выберите х или о: ')  если хотим, чтобы все же пользователь ввел правильные данные
        # mark = mark.upper()
        mark = ['X', 'O']       # если хотим быстрее началь играть :)
        mark = random.choice(mark)
        print(f'Вы ввели не то, поэтому выбор сделан за вас. Вы играете: {mark}')
        return mark
    #start_of_tic_tac_toe_game()
