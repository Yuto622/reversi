from board import Board
computer_piece=-1
board=Board()
def computer():
    i=0
    j=0
    while i<=7 and j<=7:
        if board.squares[i][j]*board.squares[i][j+1]<0 and board.squares[i][j+2]==-1:
            print(board.squares[i][j+1])
        if board.squares[i][j]*board.squares[i+1][j]<0 and board.squares[i+2][j]==-1:
            print(board.squares[i+2][j])
        


    i+=1
    j+=1