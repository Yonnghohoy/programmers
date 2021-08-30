def solution(answers):
    result = []
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for i, answer in enumerate(answers):
        if answer == m1[i%len(m1)]:
            score[0] += 1
        if answer == m2[i%len(m2)]:
            score[1] += 1
        if answer == m3[i%len(m3)]:
            score[2] += 1
    for i, s in enumerate(score):
        if s == max(score):
            result.append(i+1)
    return result