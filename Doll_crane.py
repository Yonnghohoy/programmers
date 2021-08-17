def solution(board, moves):
    list=[]
    answer = 0
    for location in moves :
        location -=1
        for i in range(len(board)):
            if board[i][location] != 0 :
                if len(list) == 0 or list[-1] != board[i][location] :
                    list.append(board[i][location])
                else:
                    list.pop(-1)
                    answer+=2
                board[i][location]=0
                break
                
    return answer