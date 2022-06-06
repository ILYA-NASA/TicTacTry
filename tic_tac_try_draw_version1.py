'''
Здесь часть от общей программы TicTacTry, которая должна рисовать 
игровое поле и результаты ходов игроков.
'''

temp_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def tic_tac_try_draw(arg_list):
    '''
    Эта функция рисует игровое поле и изменения внесёные игроком
    '''
    print("\n          TicTacTry")
    print()
    print("Ходит икрок          Номера ячеек")
    print()
    print(" {0} | {1} | {2}            1 | 2 | 3 \n"
          "===========          ===========\n"
          " {3} | {4} | {5}            4 | 5 | 6 \n"
          "===========          ===========\n"
          " {6} | {7} | {8}            7 | 8 | 9 \n".format(
              temp_list[0],
              temp_list[1],
              temp_list[2],
              temp_list[3],
              temp_list[4],
              temp_list[5],
              temp_list[6],
              temp_list[7],
              temp_list[8]
          )
          )
    print("\nВведите номер ячейки куда поставить (x или 0)\n")

tic_tac_try_draw(temp_list)
