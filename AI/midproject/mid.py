import math

# 遊戲狀態表示
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def empty_squares(self):
        return ' ' in [sq for row in self.board for sq in row]

    def make_move(self, square, letter):
        if self.board[square[0]][square[1]] == ' ':
            self.board[square[0]][square[1]] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind, col_ind = square
        row = self.board[row_ind]
        if all([s == letter for s in row]):
            return True
        # Check the column
        col = [self.board[r][col_ind] for r in range(3)]
        if all([s == letter for s in col]):
            return True
        # Check the diagonals
        if row_ind == col_ind:
            if all([self.board[i][i] == letter for i in range(3)]):
                return True
        if row_ind + col_ind == 2:
            if all([self.board[i][2-i] == letter for i in range(3)]):
                return True
        return False

# Minimax算法
def minimax(state, depth, player, alpha=-math.inf, beta=math.inf):
    max_player = 'X'  # 玩家是X
    other_player = 'O'  # 對手是O

    # 檢查是否有先前的勝利者
    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (depth + 1) if other_player == max_player else -1 * (depth + 1)}

    elif not state.empty_squares():  # 沒有空位
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -math.inf}  # 最好的最大化玩家
    else:
        best = {'position': None, 'score': math.inf}  # 最好的最小化玩家

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax(state, depth + 1, other_player, alpha, beta)  # 遞歸

        state.board[possible_move[0]][possible_move[1]] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
            alpha = max(alpha, sim_score['score'])
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
            beta = min(beta, sim_score['score'])

        if beta <= alpha:
            break

    return best

def play_game():
    game = TicTacToe()
    game.print_board()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':  # 人類玩家
            row = int(input('輸入行 (0, 1, 2): '))
            col = int(input('輸入列 (0, 1, 2): '))
            if game.make_move((row, col), letter):
                if game.current_winner:
                    print(letter + ' 贏了!')
                    break
                letter = 'X'
        else:  # 電腦玩家
            square = minimax(game, 0, letter)['position']
            game.make_move(square, letter)
            if game.current_winner:
                print(letter + ' 贏了!')
                break
            letter = 'O'

        game.print_board()

    if not game.current_winner:
        print('平局!')

if __name__ == '__main__':
    play_game()

