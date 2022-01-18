import random

class Player:

    def __init__(self, name="default", is_computer=False, grid=None, sign = ""):
        self.name = name
        self.is_computer = is_computer
        self.grid = grid
        self.sign = sign


    def get_and_validate_player_input(self):
        in_range = False
        while in_range == False:
            coord = input(str("Choose coordinates - row then column. E.g. 02 for first row, 3rd columns"))

            if len(coord) != 2 or int(coord[0]) not in range(0,3) or int(coord[1]) not in range(0,3):
                print("not valid input - grid is 3x3")
            else:
                in_range = True
                return coord

    def get_move_coord(self):
        if self.is_computer:
            coord = random.choice(["00", "01", "02", "10", "11", "12", "20", "21", "22"])
        else:
            coord = self.get_and_validate_player_input()
        return coord

    def move(self):
        changed_grid = False
        while changed_grid == False:
            coord = self.get_move_coord()
            row = int(coord[0])
            column = int(coord[1])
            if self.grid.current_state[row][column] == " ":
                self.grid.current_state[row][column] = self.sign
                changed_grid = True
                self.grid.counter += 1
                self.check_win()
                self.is_draw(self.grid.counter)

            else:
                if self.is_computer == False:
                    print("This square is already occupied")

    def check_win(self):
        if (self.grid.current_state[0][0] == self.sign and self.grid.current_state[0][1] == self.sign and self.grid.current_state[0][2] == self.sign or
        self.grid.current_state[0][0] == self.sign and self.grid.current_state[1][0] == self.sign and self.grid.current_state[2][0] == self.sign or
        self.grid.current_state[0][0] == self.sign and self.grid.current_state[1][1] == self.sign and self.grid.current_state[2][2] == self.sign or
        self.grid.current_state[0][1] == self.sign and self.grid.current_state[1][1] == self.sign and self.grid.current_state[2][1] == self.sign or
        self.grid.current_state[0][2] == self.sign and self.grid.current_state[1][2] == self.sign and self.grid.current_state[2][2] == self.sign or
        self.grid.current_state[1][0] == self.sign and self.grid.current_state[1][1] == self.sign and self.grid.current_state[1][2] == self.sign or
        self.grid.current_state[2][0] == self.sign and self.grid.current_state[2][1] == self.sign and self.grid.current_state[2][2] == self.sign or
        self.grid.current_state[0][2] == self.sign and self.grid.current_state[1][1] == self.sign and self.grid.current_state[2][0] == self.sign):
            print(f"{self.name} wins!")#
            self.grid.print_grid()
            exit(0)

    
    def is_draw(self,counter):
        if counter == 9:
            print("it's a draw!")
            self.grid.print_grid()
            exit(0)
