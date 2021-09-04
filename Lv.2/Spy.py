def solution(clothes):
    result = 0
    closet = {}
    for elem in clothes:
        key = elem[1]
        value = elem[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]
            
    for key in closet.keys():
        result = result * (len(closet[key]) + 1)
    return result - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))