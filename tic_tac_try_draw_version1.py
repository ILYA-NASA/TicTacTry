'''
Здесь часть от общей программы TicTacTry, которая должна рисовать 
игровое поле и результаты ходов игроков.
'''

temp_list = [["X", "O", "O"], ["O", "X", "X"], ["X", "O", "X"]]

def tic_tac_try_draw(arg_list):
    '''
    Эта функция рисует игровое поле и изменения внесёные игроком
    '''
#     print()
#     print("Ходит игрок {}        Номера ячеек")
    print()
    print(" {0} | {1} | {2}            1 | 2 | 3 \n"
          "===========          ===========\n"
          " {3} | {4} | {5}            4 | 5 | 6 \n"
          "===========          ===========\n"
          " {6} | {7} | {8}            7 | 8 | 9 \n".format(
              temp_list[0][0],
              temp_list[0][1],
              temp_list[0][2],
              temp_list[1][0],
              temp_list[1][1],
              temp_list[1][2],
              temp_list[2][0],
              temp_list[2][1],
              temp_list[2][2]
          )
          )

if __name__ == '__main__':
    tic_tac_try_draw(temp_list)
