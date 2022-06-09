def viktory(list_game):
    for i in range(3):
        if (list_game[i][0] ==  list_game[i][1] == list_game[i][2])  or (list_game[0][i] ==  list_game[1][i] == list_game[2][i]):
            res = True
            return res
    if (list_game[0][0] ==  list_game[1][1] == list_game[2][2])  or (list_game[-1][-1] ==  list_game[-2][-2] == list_game[-3][-3]):
        res = True
        return res
    else:
        res = False
        return res

