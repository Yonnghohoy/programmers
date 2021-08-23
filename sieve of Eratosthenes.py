def solution(n):
    lst = set(range(2,n+1))
    for i in range(2,n+1):
        if i in lst:
            lst -= set(range(i*2,n+1,i))
    answer = len(lst)
