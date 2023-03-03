import player_piece
import player
from board import Board

[x,y]=player.player_address()
player_move= player_piece.player_piece()


print(player_move)
board = Board()
print(board.squares)
board.squares[x][y] =player_move
print(board.squares)