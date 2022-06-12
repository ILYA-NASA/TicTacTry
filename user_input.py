
# import main (или controller например) 

def user_input(field,player_mark):
    from writemove import WriteMove
    while True:
        player_choice = input(f'Введите номер ячейки, чтобы поставить {player_mark}: ')
        try:
            player_choice = int(player_choice)
        except:
            print('Нужно ввести номер цифрой!')
            continue
        if player_choice >= 1 and player_choice <= 9:
            players_move = WriteMove(player_choice, player_mark,field)
            if players_move:
                break   # тут похоже нужно уходить на main и проверять было ли 5 ходов, если не было то менять mark и вызывать user_input, 
                        # если было то проверять победу, если не победа то возвращать на main и тоже менять mark и вызывать user_input
            else:
                print('Ячейка занята, будьте внимательней! ')
        else:
            print('У нас всего 9 ячеек, выберите одну из них')


# user_input('X') 
# user_input('O') 