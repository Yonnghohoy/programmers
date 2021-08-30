import itertools

def solution(nums):
    answer = 0
    lst = list(itertools.combinations(nums,3))
    sum_temp=0
    for i in range(len(lst)):
        sum_temp = sum(lst[i])
        for j in range(2,sum_temp//2 +1):
            if sum_temp % j == 0: break
            if j == sum_temp // 2:
                answer += 1
                
            

    return answer

print(solution([1,2,3,4]))