class Board:
    def __init__(self):
        self.rows1 = [[" " for cell in range(4)] for row in range(4)]
        self.rows2 = [[" " for cell in range(4)] for row in range(4)]

    def print_board(self):
        for row in range(4):
            print()
            print("+---"*8 + "+")
            print("|   | ", end="")
            for cell in range(3):
                print(self.rows1[row][cell], end=" |   | ")
            print(self.rows1[row][3], end=" |")
            print()
            print("+---"*8 + "+")
            print("| ", end="")
            for cell in range(4):
                print(self.rows2[row][cell], end=" |   | ")
        print()
        print("+---"*8 + "+")

    def set_pieces(self):
        numbers = [self.rows1[0], self.rows2[0], self.rows1[1]]
        index = 0
        for row in range(3):
            for cell in range(4):
                numbers[row][cell] = Piece(row, cell, chr(65 + index))
                index += 1

        numbers = [self.rows2[2], self.rows1[3], self.rows2[3]]
        index = 0
        for row in range(3):
            for cell in range(4):
                numbers[row][cell] = Piece(row, cell, chr(97 + index))
                index += 1

    def find_piece(self, piece):
        try:
            for row in self.rows1:
                for cell in row:
                    if cell.value == piece:
                        return cell
        except:
            for row in self.rows2:
                for cell in row:
                    if cell.value == piece:
                        return cell
        else:
            raise ValueError("Piece doesnt exist")




class Piece:
    def __init__(self, row, column, value):
        self.x = row
        self.y = column
        self.value = value

    def __repr__(self):
        return self.value



test = Board()
test.print_board()
test.set_pieces()
test.print_board()
