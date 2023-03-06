from typing import List

white=-1
black=1
empty=0

class Board:
    """
    盤面のクラス。
    最初に黒2個、白2個を配置しておく。
    """
    def __init__(self) -> None:
        self.__squares = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,-1,-1,0,0,0],
        [0,0,0,1,-1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]
    

    @property
    def squares(self) -> List:
        """
        現在のマス目の情報を返す。
        """
        return self.__squares
    
    def update(self, new_squares: List) -> List:
        """
        マス目の情報を更新する。
        """
        self.__squares = new_squares
