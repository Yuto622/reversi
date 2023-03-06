from board import Board
from game import Game
import player

[x,y]=player.player_address()

game=Game()
board=Board()

if x!=0 and y!=0 and x!=7 and y!=7:

#おこうとしている駒の場所が端ではないとき

    if board.squares[x-1][y]==0 and board.squares[x-1][y-1]==0 and board.squares[x-1][y+1]==0  and board.squares[x][y-1]==0 and board.squares[x][y+1]==0 and board.squares[x+1][y-1]==0 and board.squares[x+1][y]==0 and board.squares[x+1][y+1]==0:
        print("おける場所ではありません。")
    
    
    elif board.squares[x-1][y]==game.turn*-1 :
        #置ける可能性があります
        if board.squares[x-2][y]==game.turn*-1:
        #置ける可能性があります
        elif board.squares[x-2][y]==game.turn*1:
            print(f"{x}{y}には置けます。")
        
            if board.squares[x-3][y]==game.turn*-1:
            #置ける可能性があります
            elif board.squares[x-3][y]==game.turn*1:
                print(f"{x}{y}には置けます。")


                if board.squares[x-4][y]==game.turn*-1:
                #置ける可能性があります
                elif board.squares[x-4][y]==game.turn*1:
                    print(f"{x}{y}には置けます。")

                    if board.squares[x-5][y]==game.turn*-1:
                    #置ける可能性があります

                    elif board.squares[x-5][y]==game.turn*1:
                        print(f"{x}{y}には置けます。")


                        if board.squares[x-6][y]==game.turn*-1:
                        #置ける可能性があります

                        elif board.squares[x-6][y]==game.turn*1:
                            print(f"{x}{y}には置けます。")

                            if board.squares[x-7][y]==game.turn*1:
                                print(f"{x}{y}には置けます。")
                            else:
                                print("おけません")
                
        
        elif board.squares[x-2][y]==game.turn:
            print(f"{x}{y}には置けます。")


        


    elif board.squares[x-1][y-1]==game.turn*-1:
        print("置ける可能性があります")
    elif board.squares[x-1][y+1]==game.turn*-1:
        print("置ける可能性があります")


    elif board.squares[x][y-1]==game.turn*-1:
        print("置ける可能性があります")

    elif board.squares[x][y+1]==game.turn*-1:
        print("置ける可能性があります")

    elif board.squares[x+1][y-1]==game.turn*-1:
        print("置ける可能性があります")

    elif board.squares[x+1][y]==game.turn*-1:
        print("置ける可能性があります")

    elif board.squares[x+1][y+1]==game.turn*-1:
        print("置ける可能性があります")

        print(f"{x}{y}には置けます")
    #おこうとしている場所の隣が自分の駒以外のものの場合おける可能性がある。
        
    

     # board.squares[x-1][y]==game.turn*-1 or board.squares[x-1][y-1]==game.turn*-1 or board.squares[x-1][y+1]==game.turn*-1  or board.squares[x][y-1]==game.turn*-1 or board.squares[x][y+1]==game.turn*-1 or board.squares[x+1][y-1]==game.turn*-1 or board.squares[x+1][y]==game.turn*-1 or board.squares[x+1][y+1]==game.turn*-1:

