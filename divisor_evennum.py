def solution(left,right):
    answer = 0
    a = []
    for num in range(left,right+1):
        lst = []
        for i in range(1,num+1):
            if num % i == 0:
                lst.append(i)
        a.append(lst)
    
    for i in a:
        if len(i) % 2 == 0:
            answer += i[-1]
        else:
            answer -= i[-1]
    return answer

print(solution(13,17))