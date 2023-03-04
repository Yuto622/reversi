from typing import List
from game import Game

class View:
    """
    画面に表示させる。
    """
    def __init__(self) -> None:
        pass

    def show_board(self, squares: List) -> None:
        """
        盤面を標準出力する。
        """

        print(*squares, sep='\n')
    
    def show_turn(self, turn: int):
        """
        今が、どちらの番なのか標準出力する。
        """

        if turn==1:
            turn="黒"
        else:
            turn="白"

        return print(f"今のターンは{turn}です。")
