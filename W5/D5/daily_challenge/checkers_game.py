class Checkers:
    Nr_Game = 1
    White = ['W', 'KW']
    Black = ['B', 'KW']
    Players = ["Black", "White"]
    score = {"Black": 12, "White": 12}
    board = [
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0]],
    ]

    def display_board(self):
        for row in self.board:
            print(row)

    def initialize_game(self):
        # initiate Black
        altern = 1
        for row in range(3):
            for column in range(len(self.board[row])):
                if column % 2 == altern:
                    self.board[row][column] = self.Black[0]
            if altern == 1:
                altern -= 1
            else:
                altern = 1

        # initialize White
        altern = 0
        for row in range(5, 8):
            for column in range(len(self.board[row])):
                if column % 2 == altern:
                    self.board[row][column] = self.White[0]
            if altern == 1:
                altern -= 1
            else:
                altern = 1

    def is_king(self, row, column):
        if self.board[row][column] == self.Black[1] or self.board[row][column] == self.White[1]:
            return True
        return False

    def king_maker(self, row, column):
        if not self.is_king(row, column):
            if row == 0 or row == 7:
                if self.board[row][column] == self.Black[0]:
                    self.board[row][column] = self.Black[1]
                else:
                    if self.board[row][column] == self.White[0]:
                        self.board[row][column] = self.White[1]
        print("You have a new KING!")

    def select_row(self, player):
        row = input(f"{player}: Enter the row for the place or piece you want to select (number between 1 and 8)\n")
        row = int(row.strip())
        if 0 > row > 9:
            "chose a valid column"
            row = self.select_row(player)
        else:
            row -= 1
        return row

    def select_column(self, player):
        column = input(f"{player}: Enter the column for the place or piece you want to select (number between 1 and 8)\n")
        column = int(column.strip())
        if 0 > column > 9:
            "chose a valid row"
            column = self.select_column(player)
        else:
            column -= 1
        return column

    def select_piece(self, player):
        row = self.select_row(player)
        column = self.select_column(player)
        return row, column

    def select_move(self, player):
        row = self.select_row(player)
        column = self.select_column(player)
        return row, column

    def check_position(self, row, column):
        position = self.board[row][column]
        return position

    def is_legal_move(self, player, selected_piece, selected_move):
        if player == self.Players.index(player) and self.check_position(*selected_piece) not in self.Players.index(player):
            return "You can't select your opponents pieces!"
        elif selected_piece == selected_move:
            return "you can't move your piece to where it already is!"
        elif selected_piece[0] is not selected_move[0] and selected_piece[1] is not selected_move[1]:
            if self.check_position(*selected_move) == 0:
                return True
        else:
            return False

    def move(self, player, selected_piece, selected_move):
        old_position = self.check_position(*selected_piece)
        new_position = self.check_position(*selected_piece)
        self.check_position(*selected_move).replace(new_position, old_position)
        self.check_position(*selected_piece).replace(old_position, 0)

    def jump_normal(self, player, selected_piece, selected_move):
        if player == "Black" and selected_piece[0] > selected_move[0]:
            for r in range(selected_move[0], selected_piece[0]):
                for c in range(selected_move[1], selected_piece[1]):
                    if self.check_position(r, c) not in self.Black and not 0:
                        self.score["White"] -= 1
        if player == "White" and selected_piece[0] < selected_move[0]:
            for r in range(selected_piece[0], selected_move[0]):
                for c in range(selected_piece[0], selected_move[0]):
                    if self.check_position(r, c) not in self.White and not 0:
                        self.score["Black"] -= 1

    def jump_king(self, player, selected_piece, selected_move):
        if player == "Black":
            if selected_piece[0] > selected_move[0]:
                for r in range(selected_move[0], selected_piece[0]):
                    for c in range(selected_move[1], selected_piece[1]):
                        if self.check_position(r, c) not in self.Black and not 0:
                            self.score["White"] -= 1
            elif selected_piece[0] < selected_move[0]:
                for r in range(selected_piece[0], selected_move[0]):
                    for c in range(selected_piece[0], selected_move[0]):
                        if self.check_position(r, c) not in self.White and not 0:
                            self.score["White"] -= 1
        if player == "White":
            if selected_piece[0] > selected_move[0]:
                for r in range(selected_move[0], selected_piece[0]):
                    for c in range(selected_move[1], selected_piece[1]):
                        if self.check_position(r, c) not in self.Black and not 0:
                            self.score["Black"] -= 1
            elif selected_piece[0] < selected_move[0]:
                for r in range(selected_piece[0], selected_move[0]):
                    for c in range(selected_piece[0], selected_move[0]):
                        if self.check_position(r, c) not in self.White and not 0:
                            self.score["Black"] -= 1

    def turn(self, player):
        selected_piece = self.select_piece(player)
        selected_move = self.select_move(player)
        if self.is_legal_move(player, selected_piece, selected_move):
            if self.is_king(*selected_piece):
                self.jump_king(player, selected_piece, selected_move)
                self.move(player, selected_piece, selected_move)
            else:
                self.jump_normal(player, selected_piece, selected_move)
                self.move(player, selected_piece, selected_move)

            self.king_maker(*selected_move)
        else:
            print("That was illegal, you've lost your turn\n\n")

        print(f'the current score is: {self.score["White"]}, {self.score["Black"]}')

def main():
    game1 = Checkers()
    game1.initialize_game()
    game1.display_board()
    player = 0
    while game1.score.get("Black") > 0 and game1.score.get("White") > 0:
        if player == 0:
            game1.turn(game1.Players[0])
            player = 1
        elif player == 1:
            game1.turn(game1.Players[1])
            player = 0
        game1.display_board()
    else:
        print("Game Over!!")


if __name__ == '__main__':
    main()
