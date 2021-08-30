def solution(scores):
    answer = ''
    lst = [[0 for i in range(len(scores))] for j in range(len(scores))]
    for i in range(len(scores)):
        for j in range(len(scores)):
            lst[i][j] = scores[i][j]
    
    for i in range(len(lst)):
        if lst[i][j] == max(lst[i]) and lst[i].count(max(lst[i])) == 1:
            lst[i].pop(i)
        elif lst[i][j] == min(lst[i]) and lst[i].count(max(lst[i])) == 1:
            lst[i].pop(i)
            
        avg = sum(lst[i]) / len(lst)
        if avg >= 90 : answer +=  "A"
        elif avg >= 80 : answer +=  "B"
        elif avg >= 70 : answer +=  "C"
        elif avg >= 50 : answer +=  "D"
        else: answer += "F"
        
    return answer