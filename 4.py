
def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(row,col,left_row,upper_diag,lower_diag,N):
    return not left_row[row] and not upper_diag[row+col] and not lower_diag[row-col+N-1]

def solve_nqueen(board,col,left_row,upper_diag,lower_diag,N):
    if(col>=N):
        print_solution(board)
        return True
    found=False
    for i in range(N):
        if is_safe(i,col,left_row,upper_diag,lower_diag,N):
            board[i][col]=1
            left_row[i]=upper_diag[i+col]=lower_diag[i-col+N-1]=True

            found=solve_nqueen(board,col+1,left_row,upper_diag,lower_diag,N) or found
            board[i][col]=0
            left_row[i]=upper_diag[i+col]=lower_diag[i-col+N-1]=False
    return found

def nqueen():
    N=int(input("enter the value of N:"))
    board=[[0]*N for i in range(N)]
    left_row=[False]*N
    upper_diag=[False]*(2*N-1)
    lower_diag=[False]*(2*N-1)
    if not solve_nqueen(board,0,left_row,upper_diag,lower_diag,N):
        print("solution not exists")
nqueen()


            