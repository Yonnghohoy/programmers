def solution(s):
    check = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] == " ":
            check = 0
        else:
            if check == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            check = 1
    return "".join(s)

# print(solution("3people unFollowed me"))