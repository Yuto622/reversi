
import player
from board import Board
from game import Game
from view import View

def main():
    game = Game()
    view = View()
    i=0
    while i<=64:
        view.show_turn(turn=game.turn)
        [x,y]=player.player_address()

        board = Board()
        board.squares[x][y] = game.turn
        view.show_board(board.squares)
        game.change_turn()

main()