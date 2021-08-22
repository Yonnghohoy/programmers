def solution(s):
    se_answer=[]
    s_list = s.split(' ')
    for each_list in s_list:
        another_list = []
        for j in range(len(each_list)) :
            if j %2 ==0 : another_list.append(each_list[j].upper())
            elif j % 2 != 0: another_list.append(each_list[j].lower())
        se_answer.append("".join(another_list))
        
            
            
            
    return ' '.join(se_answer)
print(solution("try hello world"))