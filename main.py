
import player
from board import Board
from game import Game
from view import View
from model_ import Model
from status import Status


def main():
    game = Game()
    view = View()
    board = Board()
    model = Model()
    i=0
    while i<=64:
        view.show_board(board.squares)
        view.show_turn(turn=game.turn)
        x, y = player.player_address()
        status = Status(t=game.turn, p=(x, y), s=board.squares)
        if model.check_direction(status):
            print(f"{(x, y)}におくことができます")
            model.check_flip(status=status)
            # new_squares = model.flip_tile(status)
            # board.update(new_squares=new_squares)
        else:
            print("おけません")
            break

        # board.squares[x][y] = game.turn
        # game.change_turn()

main()