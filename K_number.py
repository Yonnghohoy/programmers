def solution(array, commands):
    answer=[]
    for elem in commands:
        tmp = array[elem[0]-1:elem[1]]
        tmp.sort()
        answer.append(tmp[elem[2]-1])
    return answer