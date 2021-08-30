dis_from_2 = {1:1,2:0,3:1,4:2,5:1,6:2,7:3,8:2,9:3,0:3,"#":4,"*":4}
dis_from_5 = {1:2,2:1,3:2,4:1,5:0,6:1,7:2,8:1,9:2,0:2,"#":3,"*":3}
dis_from_8 = {1:3,2:2,3:3,4:2,5:1,6:2,7:1,8:8,9:1,0:1,"#":2,"*":2}
dis_from_0 = {1:4,2:3,3:4,4:3,5:2,6:3,7:2,8:1,9:2,0:0,"#":1,"*":1}

def solution(numbers,hand):
    answer=""
    loc_left = "*"
    loc_right = "#"
    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            loc_left = n
        elif n in [3,6,9]:
            answer += "R"
            loc_right = n
        else:
            dic = dis_from_2 if n == 2 else dis_from_5 if n == 5 else dis_from_8 if n == 8 else dis_from_0
            if dic[loc_left] < dic[loc_right]:
                answer += "L"
                loc_left = n
            elif dic[loc_left] > dic[loc_right]:
                answer += "R"
                loc_right = n
            else:
                if hand == "right":
                    answer += "R"
                    loc_right = n
                else:
                    answer += "L"
                    loc_left = n        
    return answer