def solution(scores):
    answer = []
    for j in range(len(scores)):
        scores_list=[]
        for i in range(len(scores)):
            scores_list.append(scores[i][j])
        if scores_list[j] in [max(scores_list), min(scores_list)]:
            scores_list.remove(scores_list[j])
        answer.append(sum(scores_list)/len(scores_list))
    for i in range(len(answer)):
        if answer[i] >= 90:
            answer[i] = 'A'
        elif answer[i] >= 80:
            answer[i] = 'B'
        elif answer[i] >= 70:
            answer[i] = 'C'
        elif answer[i] >= 50:
            answer[i] = 'D'
        else:
            answer[i] = 'F'
    return answer