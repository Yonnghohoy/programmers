def solution(array, commands):
    answer=''
    for elem in commands:
        tmp = array[elem[0]:elem[5+1]]
        tmp.sort()
        answer+=tmp[elem[2]]
    return answer