# Ввод пользователя.Проверка заполненности ячейки. 
# (вход list, метка (X или О, или bool), выход int:1-9,метка,list (совпадает со входом на 6)
# нумерация
#     1 2 3
#     4 5 6
#     7 8 9
# наполнение
#   ("X ,"O"," ") (заглавная латиница)

def user_input(player_mark, count):
    players_move = True
    while players_move:
        player_choice = input(f'Введите номер ячейки, чтобы поставить {player_mark}: ')
        try:
            player_choice = int(player_choice)
        except:
            print('Нужно ввести номер цифрой!')
            continue
        if player_choice >= 1 and player_choice <= 9:
            if str(field_list[player_choice-1]) not in 'X' 'O': # так можно сравнить не цифры а строки 
                field_list[player_choice-1] = player_mark # то, о чем я писал на гитхабе, не обязательно лист на вход брать, можно вне функции значения последовательности менять 
                print(field_list[:3]) # принты тут для наглядности 
                print(field_list[3:6])
                print(field_list[6:])
                count += 1 # в модуле проверки победы можно count считать, player_mark менять и поле заполнять (тогда и на входе count не нужен будет)
                if count <= 5:
                    if count % 2 == 0:
                        user_input('X', count) 
                    else:
                        user_input('O', count)
                else:
                    players_move = False # почему-то из цикла не выходит после пяти попыток, но это не важно если счетчик вынесем в другой модуль
            else:
                print('Ячейка занята, будьте внимательней! ')
        else:
            print('У нас всего 9 ячеек, выберите одну из них')


field_list = [1, 'X', '3', 4, 'O', 6, ' ', 8, 9]
print(field_list[:3])
print(field_list[3:6])
print(field_list[6:])

user_input('X', 0) 