import consts
def build_game_board(game_board):
    for row in range(25):
        row_list = []
        for col in range(50):
            row_list.append('')
        game_board.append(row_list)
    print(game_board)
    return game_board
build_game_board(consts.game_board)

