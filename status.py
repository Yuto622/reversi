from typing import List


class Status:
    """
    ターンの状況を保持したクラス。
    """
    def __init__(self, t: int, p: tuple, s: List) -> None:
        self.__turn = t
        self.__position = p
        self.__squares = s

    @property
    def turn(self) -> int:
        return self.__turn

    @property
    def position(self) -> tuple:
        return self.__position

    @property
    def squares(self) -> List:
        return self.__squares
        
        