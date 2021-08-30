def solution(n):
    answer = list(str(n))
    answer = list(map(int,answer))
    answer = sum(answer)
    return answer

print(solution(123))


# def solution(n):
#     return sum(map(int, list(str(n))))