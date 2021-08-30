def solution(s):
    str = list(s)
    str.sort(reverse=True)
    return ''.join(str)
print(solution('Zbcdefg'))