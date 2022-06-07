# 2. Ввод пользователя. Проверка заполненности ячейки. 
# (вход bool: метка (X или О), выход list, выход int:1-9, метка (X или О)) 
# нумерация  
#     1 2 3
#     4 5 6
#     7 8 9
# наполнение
#   ("X ,"O"," ") (заглавная латиница)

def user_input(player_mark, field_list): # похоже, что field_list надо заполнять вне функции и брать на вход 
    if player_mark == True: # лучше конечно player_mark сразу str а не bool 
        player_mark = 'X'
    else:
        player_mark = 'O'
    players_move = True
    while players_move:        
        player_choice = input(f'Введите номер ячейки, чтобы поставить {player_mark}: ')
        try:
            player_choice = int(player_choice)
        except:
            print('Нужно ввести номер цифрой!')
            continue

        if player_choice >= 1 and player_choice <= 9:
            for choice in field_list:
                if choice != player_choice:
                    field_list.append(player_choice)
                else:
                    print('Ячейка занята, будьте внимательней! ')
            players_move = False
            return field_list, player_choice, player_mark 
        else:
            print('У нас всего 9 ячеек, выберите одну из них')

print(user_input(True, []))
# print(user_input(False, []))