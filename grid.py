class Grid:

    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.current_state = [3*[".", ".", "."]]  #to track which ones are occupied



    #def check_if_empty(self,row,col):
    def print_grid(self):
        print(self.current_state)
