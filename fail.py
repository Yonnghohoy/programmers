def solution (n, stages):
    lst = {}
    length = len(stages)
    for i in range(1,n+1):
        if length != 0:
            cnt = stages.count(i)
            lst[i] = cnt / length
            length -= cnt
        else : 
            lst[i] = 0
            
    
    arr = sorted(list(lst.keys()))
    
    return arr

print(solution(5,[2,1,2,6,2,4,3,3]))
            