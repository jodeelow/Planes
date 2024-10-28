from src.board import *
import random
import copy


class ComputerPlayer:
    def __init__(self, player_board: PlayerBoard, target_board: TargetBoard):
        self.__player_board = player_board
        self.__target_board = target_board
        self.__shots = []
        for i in range(10):
            for j in range(10):
                self.__shots.append([i, j])

    def add_planes_computer(self, symbol: str = '#'):
        """
        randomly adds a plane on ai's player map
        :param symbol: pilot's cabins
        :return: plane's pilot's cabin coordinates and its direction
        """
        number_of_filled_squares = 0
        copy_of_board = copy.deepcopy(self.__player_board)
        directions = ["up", "right", "down", "left"]
        direction = random.choice(directions)
        row = random.randint(0, 9)
        column = random.randint(0, 9)

        if not (0 <= row < 10):
            raise PlaneError("Invalid row!")

        if not (0 <= column < 10):
            raise PlaneError("Invalid column!")

        if (0 <= row < 10) and (0 <= column < 10):

            if direction == "up":
                if not ((10 - row - 1) >= 3) or not ((10 - column - 1) >= 2) or not (column >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__player_board.get_board()[row][column] = symbol
                    for i in range(3):
                        self.__player_board.get_board()[row + i + 1][column] = '*'
                    self.__player_board.get_board()[row + 3][column - 1] = '*'
                    self.__player_board.get_board()[row + 3][column + 1] = '*'
                    for i in range(2):
                        self.__player_board.get_board()[row + 1][column - i - 1] = '*'
                        self.__player_board.get_board()[row + 1][column + i + 1] = '*'
                    for i in range(10):
                        for j in range(10):
                            if (self.__player_board.get_board()[i][j] == '*') or (self.__player_board.get_board()[i][j] == symbol):
                                number_of_filled_squares += 1
                    if (number_of_filled_squares != 0) and (number_of_filled_squares != 10) and (number_of_filled_squares != 20) and (number_of_filled_squares != 30):
                        self.__player_board = copy_of_board
                        raise PlaneError("This plane crosses another, try again!")

            elif direction == "right":
                if not (column >= 3) or not (row >= 2) or not ((10 - row - 1) >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__player_board.get_board()[row][column] = symbol
                    for i in range(3):
                        self.__player_board.get_board()[row][column - i - 1] = '*'
                    self.__player_board.get_board()[row - 1][column - 3] = '*'
                    self.__player_board.get_board()[row + 1][column - 3] = '*'
                    for i in range(2):
                        self.__player_board.get_board()[row - i - 1][column - 1] = '*'
                        self.__player_board.get_board()[row + i + 1][column - 1] = '*'
                    for i in range(10):
                        for j in range(10):
                            if (self.__player_board.get_board()[i][j] == '*') or (self.__player_board.get_board()[i][j] == symbol):
                                number_of_filled_squares += 1
                    if (number_of_filled_squares != 0) and (number_of_filled_squares != 10) and (number_of_filled_squares != 20) and (number_of_filled_squares != 30):
                        self.__player_board = copy_of_board
                        raise PlaneError("This plane crosses another, try again!")

            elif direction == "down":
                if not (column >= 2) or not (row >= 3) or not ((10 - column - 1) >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__player_board.get_board()[row][column] = symbol
                    for i in range(3):
                        self.__player_board.get_board()[row - i - 1][column] = '*'
                    self.__player_board.get_board()[row - 3][column - 1] = '*'
                    self.__player_board.get_board()[row - 3][column + 1] = '*'
                    for i in range(2):
                        self.__player_board.get_board()[row - 1][column - i - 1] = '*'
                        self.__player_board.get_board()[row - 1][column + i + 1] = '*'
                    for i in range(10):
                        for j in range(10):
                            if (self.__player_board.get_board()[i][j] == '*') or (self.__player_board.get_board()[i][j] == symbol):
                                number_of_filled_squares += 1
                    if (number_of_filled_squares != 0) and (number_of_filled_squares != 10) and (number_of_filled_squares != 20) and (number_of_filled_squares != 30):
                        self.__player_board = copy_of_board
                        raise PlaneError("This plane crosses another, try again!")

            elif direction == "left":
                if not (column <= 6) or not (row >= 2) or not ((10 - row - 1) >= 2):
                    raise PlaneError("Plane doesn't fit the board!")
                else:
                    self.__player_board.get_board()[row][column] = symbol
                    for i in range(3):
                        self.__player_board.get_board()[row][column + i + 1] = '*'
                    self.__player_board.get_board()[row - 1][column + 3] = '*'
                    self.__player_board.get_board()[row + 1][column + 3] = '*'
                    for i in range(2):
                        self.__player_board.get_board()[row - i - 1][column + 1] = '*'
                        self.__player_board.get_board()[row + i + 1][column + 1] = '*'
                    for i in range(10):
                        for j in range(10):
                            if (self.__player_board.get_board()[i][j] == '*') or (self.__player_board.get_board()[i][j] == symbol):
                                number_of_filled_squares += 1
                    if (number_of_filled_squares != 0) and (number_of_filled_squares != 10) and (number_of_filled_squares != 20) and (number_of_filled_squares != 30):
                        self.__player_board = copy_of_board
                        raise PlaneError("This plane crosses another, try again!")

            else:
                raise PlaneError("Invalid direction!")

        return [row, column, direction]

    def fire_shot(self, opponent_board, human_plane_1, human_plane_2, human_plane3):
        """
        marks the attacked square on the target board with '*' if it was a part of the plane there, 'o' if not
        marks the whole plane with '*', if it was a cabin shot
        :param opponent_board: human player's player board
        :param human_plane_1: player's plane, contains cabin's coordinates and plane's direction on the map
        :param human_plane_2: player's plane, contains cabin's coordinates and plane's direction on the map
        :param human_plane3: player's plane, contains cabin's coordinates and plane's direction on the map
        :return:
        """
        square = random.choice(self.__shots)
        x = square[0]
        y = square[1]
        self.__target_board.fire_shot(opponent_board, x, y, human_plane_1, human_plane_2, human_plane3)
        for i in range(10):
            for j in range(10):
                if self.__target_board.get_board()[i][j] == '*' or self.__target_board.get_board()[i][j] == 'o':
                    try:
                        self.__shots.remove([i, j])
                    except ValueError:
                        pass
        return [x, y]

    def get_player_board(self):
        """
        :return: ai's player board
        """
        return self.__player_board

    def get_target_board(self):
        """
        :return: ai's target board
        """
        return self.__target_board

    def get_shots(self):
        """
        :return: ai's remaining location where to fire a shot
        """
        return self.__shots
