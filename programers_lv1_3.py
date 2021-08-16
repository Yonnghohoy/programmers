def solution(s):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i, num in enumerate(numbers):
        s = s.replace(num, str(i))
    return int(s)