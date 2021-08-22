def solution(n):
    answer = []
    answer = list(map(int, reversed(str(n))))
    
    return answer

print(solution(12345))