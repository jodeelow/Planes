from texttable import Texttable
import unittest
import copy


class PlaneError(Exception):
    pass


class Board:
    def __init__(self, height: int = 10, width: int = 10):
        """
        Board's representation: '#' - pilot's cabin
                                '*' - plane's body
                                ' ' - empty space on board
        :param height:
        :param width:
        """
        self.__height = height
        self.__width = width
        self.__board = [[' ' for i in range(width)]for j in range(height)]

    def get_board(self):
        """
        :return: board's matrix representation
        """
        return self.__board

    def add_plane(self, row, column, direction, symbol: str = '#'):
        """
        adds a plane on the board by telling the method pilot's cabin coordinates and plane's direction
        if the point/square is outside the board, or the plane doesn't fit in the board, it raises PlaneError
        :param row: square's row
        :param column: square's column
        :param direction: plane's direction
        :param symbol: the symbol indicating the pilot's cabin
        :return: nothing
        """

        number_of_filled_squares = 0
        copy_of_board = copy.deepcopy(self.__board)

        if not(0 <= row < self.__height):
            raise PlaneError("Invalid row!")

        if not(0 <= column < self.__width):
            raise PlaneError("Invalid column!")

        if (0 <= row < self.__height) and (0 <= column < self.__width):

            if direction == "up":
                if not((self.__height - row - 1) >= 3) or not((self.__width - column - 1) >= 2) or not(column >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__board[row][column] = symbol
                    for i in range(3):
                        self.__board[row + i + 1][column] = '*'
                    self.__board[row + 3][column - 1] = '*'
                    self.__board[row + 3][column + 1] = '*'
                    for i in range(2):
                        self.__board[row + 1][column - i - 1] = '*'
                        self.__board[row + 1][column + i + 1] = '*'

            elif direction == "right":
                if not(column >= 3) or not(row >= 2) or not((self.__height - row - 1) >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__board[row][column] = symbol
                    for i in range(3):
                        self.__board[row][column - i - 1] = '*'
                    self.__board[row - 1][column - 3] = '*'
                    self.__board[row + 1][column - 3] = '*'
                    for i in range(2):
                        self.__board[row - i - 1][column - 1] = '*'
                        self.__board[row + i + 1][column - 1] = '*'

            elif direction == "down":
                if not(column >= 2) or not(row >= 3) or not((self.__width - column - 1) >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__board[row][column] = symbol
                    for i in range(3):
                        self.__board[row - i -1][column] = '*'
                    self.__board[row - 3][column - 1] = '*'
                    self.__board[row - 3][column + 1] = '*'
                    for i in range(2):
                        self.__board[row - 1][column - i - 1] = '*'
                        self.__board[row - 1][column + i + 1] = '*'

            elif direction == "left":
                if not(column <= 6) or not(row >= 2) or not((self.__height - row - 1) >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__board[row][column] = symbol
                    for i in range(3):
                        self.__board[row][column + i + 1] = '*'
                    self.__board[row - 1][column + 3] = '*'
                    self.__board[row + 1][column + 3] = '*'
                    for i in range(2):
                        self.__board[row - i - 1][column + 1] = '*'
                        self.__board[row + i + 1][column + 1] = '*'

            else:
                raise PlaneError("Invalid direction!")

    def __eq__(self, other):
        return self.__board == other.get_board()

    def valid_plane(self, symbol):
        """
        verifies if the recently added plane doesn't cross another one. If it does, PlaneError is raised, else the plane
        remains on the board
        :param symbol: pilot's cabin square
        :return:
        """
        number_of_filled_squares = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if (self.__board[i][j] == '*') or (self.__board[i][j] == symbol):
                    number_of_filled_squares += 1
        if (number_of_filled_squares != 0) and (number_of_filled_squares != 10) and (number_of_filled_squares != 20) and (number_of_filled_squares != 30):
            # self.__board = copy_of_board
            raise PlaneError("This plane crosses another, try again!")

    def get_width(self):
        """
        :return: board's width
        """
        return self.__width

    def get_height(self):
        """
        :return: board's height
        """
        return self.__height

    @property
    def set_board(self):
        return self.__board

    @set_board.setter
    def set_board(self, new_board: list[list[str]]):
        self.__board = new_board

    def __str__(self):
        t = Texttable()
        trow = ['/']
        for i in range(self.__width):
            trow.append(chr(ord('A') + i))
        t.header(trow)
        for i in range(self.__height):
            t.add_row([i + 1] + self.__board[i])
        return t.draw()


class PlayerBoard(Board):
    pass


class TargetBoard(Board):

    def fire_shot(self, opponent_board, x, y, plane1, plane2, plane3):
        """
        marks the attacked square on the target board with '*' if it was a part of the plane there, 'o' if not
        marks the whole plane with '*', if it was a cabin shot
        :param opponent_board: opponent's player board
        :param x: square's row that you want to attack
        :param y: square's column that you want to attack
        :param plane1: opponent's plane, contains cabin's coordinates and plane's direction on the map
        :param plane2: opponent's plane, contains cabin's coordinates and plane's direction on the map
        :param plane3: opponent's plane, contains cabin's coordinates and plane's direction on the map
        :return:
        """
        hit = False
        if (opponent_board[x][y] == '*') or (opponent_board[x][y] == '#'):
            hit = True
        if hit == True:
            if opponent_board[x][y] == '#':
                if x == plane1[0] and y == plane1[1]:
                    self.add_plane(x, y, plane1[2], '*')
                elif x == plane2[0] and y == plane2[1]:
                    self.add_plane(x, y, plane2[2], '*')
                elif x == plane3[0] and y == plane3[1]:
                    self.add_plane(x, y, plane3[2], '*')
            else:
                self.get_board()[x][y] = '*'
        else:
            self.get_board()[x][y] = 'o'


class Test(unittest.TestCase):
    def test_add_plane(self):
        """
        tests the add_plane method from class Board/PlayerBoard
        :return:
        """
        test = Board(10, 10)
        test.add_plane(0, 2, "up", '#')
        test1 = Board(10, 10)
        # test1.get_board()[2][2] = '*'
        # self.assertEqual(test, test1)
        test1.get_board()[1][0] = '*'
        test1.get_board()[1][1] = '*'
        test1.get_board()[1][2] = '*'
        test1.get_board()[1][3] = '*'
        test1.get_board()[1][4] = '*'
        test1.get_board()[0][2] = '#'
        test1.get_board()[2][2] = '*'
        test1.get_board()[3][1] = '*'
        test1.get_board()[3][2] = '*'
        test1.get_board()[3][3] = '*'
        self.assertEqual(test, test1)


# t = Test()
# t.test_add_plane()
# t.test_fire_shot()
# b = Board()
# print(b)

