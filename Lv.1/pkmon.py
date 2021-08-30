def solution(nums):
    answer = 0
    
    _nums = set(nums)
    numbers = len(nums)/2
    if len(_nums) >= numbers :
        answer = numbers
    elif len(_nums) < numbers :
        answer = len(_nums)
    return answer