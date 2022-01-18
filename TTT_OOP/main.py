from player import Player
from grid import Grid

if __name__ == "__main__":
    print("Let's play TikTakToe!")

    print("please type in coordinates where you want to set your X")

    grid = Grid()

    player = Player(name=input(f"your name: "), is_computer=False,grid=grid, sign = "X")
    computer = Player(name="Computer", is_computer=True,grid=grid, sign = "O")


    while True:
        grid.print_grid()
        player.move()
        computer.move()
        #grid.print_grid()
