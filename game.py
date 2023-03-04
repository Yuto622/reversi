
class Game:
    """
    ・順番を保持する
    """
    def __init__(self) -> None:
        self.__turn = 1 #  黒：1, 白：-1

    @property
    def turn(self) -> int:
        """
        いま、黒の番か、白の番かを返す。
        """
        return self.__turn
    
    def change_turn(self)-> None:
        """
        次の番に変える。
        """
        if self.__turn == 1:
            self.__turn = -1
        else:
            self.__turn = 1
    
    