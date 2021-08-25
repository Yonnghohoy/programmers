def solution(d,budget):
    d.sort()
    answer = 0
    for i in range(len(d)):
        if sum(d[:i+1]) <= budget: 
            answer += 1
        else: 
            break
            
    return answer