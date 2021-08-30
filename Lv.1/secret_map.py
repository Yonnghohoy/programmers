def solution(n,arr1,arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:]
        b = "0"*(n-len(a)) + a
        b = b.replace("1","#")
        b = b.replace("0"," ")
        answer.append(b)
    return answer
print(solution(6,[46, 33, 33 ,22, 31, 50],	[27 ,56, 19, 14, 14, 10]))