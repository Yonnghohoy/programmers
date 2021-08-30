def solution(n):
    
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else: answer += "박"
    return answer


# def solution(n):
#     str ="수박"
    
#     if n % 2 == 0:
#         return str*(n//2)
#     else : return str*(n//2)+str[0]