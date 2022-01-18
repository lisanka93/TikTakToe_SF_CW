class Grid:

    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.current_state = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]  #to track which ones are occupied
        self.counter = 0


    #def check_if_empty(self,row,col):
    def print_grid(self):
        for i in self.current_state:
            print(i)
        print()

    def restart(self):
        new_game = input("Do you want to play another game? Y/N").lower()

        if new_game == "y":
            return True
        else:
            return False
