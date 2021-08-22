from math import gcd, lcm

def gcd(x,y):
    while y:
        x,y = y, x%y
    return x

def solution(n, m):
    answer = []
    for i in range(len(n)):
        answer.append(gcd(n,m))
        answer.append(lcm(n,m))
    return answer