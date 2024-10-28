from src.board import *
from src.computer_player import *
import copy


class UI:
    def __init__(self):
        self.__player_board = PlayerBoard()
        self.__player_target_board = TargetBoard()
        self.__p_board_ai = PlayerBoard()
        self.__t_board_ai = TargetBoard()
        self.__computer = ComputerPlayer(self.__p_board_ai, self.__t_board_ai)

    def start(self):

        planes_p = []
        planes_c = []

        i = 0

        print(self.__player_board)

        # player places his planes
        while i < 3:
            copy_of_board = copy.deepcopy(self.__player_board)
            try:
                x = int(input("Enter pilot's cabin row: "))
                y = str(input("Enter pilot's cabin column: "))
                x = x - 1
                y = ord(y) - ord('A')
                direction = str(input("Enter plane's direction: "))
                self.__player_board.add_plane(x, y, direction, '#')
                self.__player_board.valid_plane('#')
                planes_p.append([x, y, direction])
                i += 1
            except PlaneError as p:
                print("This plane crosses another one or doesn't fit the board, try again!")
                self.__player_board = copy_of_board
            print(self.__player_board)
            # print(planes_p)
            # print(self.__player_target_board)
        player_remaining_planes = 3

        # ai places its planes
        i = 0
        directions = ["up", "right", "down", "left"]
        while i < 3:
            try:
                direction = random.choice(directions)
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                plane = self.__computer.add_planes_computer('#')
                planes_c.append(plane)
                i += 1
            except PlaneError as p:
                pass

        nr1 = 0
        nr2 = 0
        for i in range(10):
            for j in range(10):
                if self.__computer.get_player_board().get_board()[i][j] == '#':
                    nr1 += 1
                elif self.__computer.get_player_board().get_board()[i][j] == '*':
                    nr2 += 1

        if nr1 == 2 and nr2 == 18:
            i = 0
            while i < 1:
                try:
                    direction = random.choice(directions)
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    plane = self.__computer.add_planes_computer('#')
                    planes_c[2] = plane
                    i += 1
                except PlaneError as p:
                    pass

        # print(self.__computer.get_player_board())
        # print(planes_c)
        computer_remaining_planes = 3

        choice = str(input("Do you want to make the first move? "))

        if choice == "yes":
            moves = 0
            while player_remaining_planes > 0 and computer_remaining_planes > 0:
                x = int(input("Enter shot's row: "))
                y = str(input("Enter shot's column: "))
                x = x - 1
                y = ord(y) - ord('A')
                self.__player_target_board.fire_shot(self.__computer.get_player_board().get_board(), x, y, planes_c[0], planes_c[1], planes_c[2])
                if self.__computer.get_player_board().get_board()[x][y] == '#':
                    computer_remaining_planes -= 1
                print("Computer's remaining planes: ")
                print(computer_remaining_planes)
                print("Your target board: ")
                print(self.__player_target_board)

                moves += 1
                ai_shot_square = self.__computer.fire_shot(self.__player_board.get_board(), planes_p[0], planes_p[1], planes_p[2])
                x = ai_shot_square[0]
                y = ai_shot_square[1]
                if self.__player_board.get_board()[x][y] == '#':
                    player_remaining_planes -= 1

                # print("Player's remaining planes: ")
                # print(player_remaining_planes)
                # print("AI's target board: ")
                # print(self.__computer.get_target_board())
                print("AI's moves: ")
                print(moves)

            if computer_remaining_planes == 0:
                print("You won!")

            elif player_remaining_planes == 0:
                print("You lost!")

        elif choice == "no":
            moves = 0
            while player_remaining_planes > 0 and computer_remaining_planes > 0:
                moves += 1
                ai_shot_square = self.__computer.fire_shot(self.__player_board.get_board(), planes_p[0], planes_p[1], planes_p[2])
                x = ai_shot_square[0]
                y = ai_shot_square[1]
                if self.__player_board.get_board()[x][y] == '#':
                    player_remaining_planes -= 1

                # print("Player's remaining planes: ")
                # print(player_remaining_planes)
                # print("AI's target board: ")
                # print(self.__computer.get_target_board())
                print("AI's moves: ")
                print(moves)
                # print("square shot: ")
                # print(ai_shot_square)

                x = int(input("Enter shot's row: "))
                y = str(input("Enter shot's column: "))
                x = x - 1
                y = ord(y) - ord('A')
                self.__player_target_board.fire_shot(self.__computer.get_player_board().get_board(), x, y, planes_c[0], planes_c[1], planes_c[2])
                if self.__computer.get_player_board().get_board()[x][y] == '#':
                    computer_remaining_planes -= 1
                print("Computer's remaining planes: ")
                print(computer_remaining_planes)
                print("Your target board: ")
                print(self.__player_target_board)

            if computer_remaining_planes == 0:
                print("You won!")

            elif player_remaining_planes == 0:
                print("You lost!")

        else:
            print("Invalid input, try again!")


ui = UI()
ui.start()
