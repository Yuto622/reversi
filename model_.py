from typing import List
from status import Status
from game import Game


class Model:
    """
    オセロのルールを司るクラス。
    """
    def __init__(self) -> None:
        pass

    def check_flip(self, status: Status) -> bool:
        """
        入力された箇所に置かれた時、ひっくり返せるかどうか

        """
        game=Game()
        x, y = status.position
        flip_position = self.different_tile(status=status)
        for position in flip_position:
            
            direction = (position[0] - x, position[1] - y)
            next_flip = (position[0] + direction[0], position[1] + direction[1])
            print(position)
            print(next_flip)

            if status.turn * status.squares[next_flip[0]][next_flip[1]] > 0:
                print("ひっくり返せる")
                status.squares[position[0]][position[1]] = status.squares[position[0]][position[1]] * -game.turn
                return True

                

                continue

            elif status.squares[next_flip[0]][next_flip[1]]==0:
                print("一番向こう側が空のためおけません")
                return False
                continue

            elif status.turn * status.squares[next_flip[0]][next_flip[1]] < 0:
                print("探索を続ける")
                next_next_flip=(position[0]+2*direction[0],position[1]+2*direction[1])
                print(next_next_flip)



                if status.turn * status.squares[next_next_flip[0]][next_next_flip[1]] > 0:
                    print("ひっくり返せる")
                    status.squares[position[0]][position[1]] = status.squares[position[0]][position[1]] * -game.turn
                    status.squares[next_flip[0]][next_flip[1]] = status.squares[next_flip[0]][next_flip[1]] * -game.turn
                    return True
                    continue

                elif status.squares[next_next_flip[0]][next_next_flip[1]]==0:
                    print("一番向こう側が空のためおけません")
                    return False
                    continue

                elif status.turn * status.squares[next_next_flip[0]][next_next_flip[1]] < 0:
                    print("探索を続ける")
                    next_next_next_flip=(position[0]+3*direction[0],position[1]+3*direction[1])
                    print(next_next_next_flip)

                    if status.turn * status.squares[next_next_next_flip[0]][next_next_next_flip[1]] > 0:
                        print("ひっくり返せる")
                        status.squares[position[0]][position[1]] = status.squares[position[0]][position[1]] * -game.turn
                        status.squares[next_flip[0]][next_flip[1]] = status.squares[next_flip[0]][next_flip[1]] * -game.turn
                        status.squares[next_next_flip[0]][next_next_flip[1]] = status.squares[next_next_flip[0]][next_next_flip[1]] * -game.turn
                        return True
                        continue

                    elif status.squares[next_next_next_flip[0]][next_next_next_flip[1]]==0:
                        print("一番向こう側が空のためおけません")
                        return False
                        continue

                    elif status.turn * status.squares[next_next_next_flip[0]][next_next_next_flip[1]] < 0:
                        print("探索を続ける")
                        next_next_next_next_flip=(position[0]+4*direction[0],position[1]+4*direction[1])
                        print(next_next_next_next_flip)
                    
                        if status.turn * status.squares[next_next_next_next_flip[0]][next_next_next_next_flip[1]] > 0:
                            print("ひっくり返せる")
                            status.squares[position[0]][position[1]] = status.squares[position[0]][position[1]] * -game.turn
                            status.squares[next_flip[0]][next_flip[1]] = status.squares[next_flip[0]][next_flip[1]] * -game.turn
                            status.squares[next_next_flip[0]][next_next_flip[1]] = status.squares[next_next_flip[0]][next_next_flip[1]] * -game.turn
                            status.squares[next_next_next_flip[0]][next_next_next_flip[1]] = status.squares[next_next_next_flip[0]][next_next_next_flip[1]] * -game.turn
                            return True
                            continue
                        elif status.turn * status.squares[next_next_next_next_flip[0]][next_next_next_next_flip[1]] < 0:
                            print("探索を続ける")
                        else:
                            print("一番向こう側が空なのでおくことが出来ません")
                            return False
                            continue
            

            else:
                print("一番向こう側が空のためおけません")
                return False
                continue
    
        

    def check_direction(self, status: Status) -> bool:
        """
        隣り合う駒が違う色かどうかをチェックする。
        """
        move_position = self.different_tile(status=status)

        return len(move_position) > 0
       
        # while y < 8:
        #     if turn * squares[x][y + 1] < 0 and turn * squares[x][y + 2] > 0:
        #         return True
        
        # elif turn * squares[x][y + 1] < 0 and turn * squares[x][y + 2] < 0 and turn * squares[x][y + 3] > 0:
        #     return True
        
    def different_tile(self, status: Status) -> List:
        x, y = status.position
        directions = [
            (x - 1, y),  # 上
            (x - 1, y + 1), # 右上
            (x, y + 1),  # 右
            (x + 1, y + 1),  # 右下
            (x + 1, y),  # 下
            (x + 1, y - 1),  # 左下
            (x, y - 1),  # 左
            (x - 1, y - 1),  # 左上
        ]

        move_postion = []
        for d in directions:
            a, b = d
            if status.turn * status.squares[a][b] < 0:
                move_postion.append((a, b))
        return move_postion
    
    
            
        
                
        
            