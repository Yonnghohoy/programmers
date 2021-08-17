def solution(n, lost, reserve):
    real_lost=[]
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            real_lost.append(i)
    answer = n-len(real_lost)
    real_lost.sort()
    
    for i in real_lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
            
    return answer