

def BotMove(field,mark):
    return mark

def ConsoleTicTac():
    from start_of_game import start_of_tic_tac_toe_game as Start
    from tic_tac_try_draw_version1 import tic_tac_try_draw as Draw
    from user_input import user_input as PlayerMove
    from vin_check import viktory as IsWin
    # from writemove import WriteMove
    player_choice = Start()
    use_bot = False
    if player_choice[1] == True : use_bot == True #подключаем потом модуль бота от этого флага.
    if player_choice[0] == 'X': 
        player_num = 1 #Если будем поздравлять конкретного игрока в выходе,используем эту переменную
        bot_turn = 2
    else:
        player_num = 2
        bot_turn = 1
    player_mark = "X"
    move_count = 0
    list_game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    game_end = False
    while move_count < 9 :
        if use_bot == True:
            if bot_turn == 1:
                BotMove(list_game,player_mark)
                bot_turn = 2
            else :
                Draw(list_game)
                PlayerMove(list_game,player_mark)
                bot_turn = 1
        else:
            Draw(list_game)
            PlayerMove(list_game,player_mark)
        
        move_count +=1
        if move_count >= 5:
            game_end = IsWin(list_game)
            if game_end == True:
                Draw(list_game)
                return print(f"Победили {player_mark}-ики!")
        if player_mark == 'X' : player_mark = 'O'
        else: player_mark = 'X'
        
    Draw(list_game)
    return print(f"Игра закончилась, ничья!")

ConsoleTicTac()

    
