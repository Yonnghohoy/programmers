def solution(lottos, win_nums):
    cnt = 0
    for nums in lottos:
        if nums in win_nums:
            cnt +=1
    answer = [cnt+lottos.count(0),cnt]
    for i in range(2):
        if answer[i] == 6 :
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] ==4:
            answer[i] = 3
        elif answer[i]== 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else : answer[i] = 6

    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))