def solution(nums):
    answer = 0
    
    _nums = set(nums)
    numbers = len(nums)/2
    if len(_nums) >=numbers :
        answer =len(_nums)
    elif len(_nums) < numbers :
        answer =len(nums)
    return answer