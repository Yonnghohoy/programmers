from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)

print(solution([2,1,3,4,1]))