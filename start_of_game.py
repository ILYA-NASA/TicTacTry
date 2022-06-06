def start_of_tic_tac_toe_game():
    
    mark = input('Вы будете играть крестиками (X) или ноликами (O)? ')
    mark = mark.upper()
    
    while True:
        if mark == 'X':
            return True
        if mark == 'O':
            return False
        mark = input('Вы ввели не те знаки. Выберите х или о: ')
        mark = mark.upper()

start_of_tic_tac_toe_game()
