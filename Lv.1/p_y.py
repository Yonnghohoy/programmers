def solution(s):
    return True if s.count('p') + s.count('P') == s.count('y') + s.count("Y") else False

# p_count = s.count("p") + s.count("P")
# s_count = s.count("y") + s.count("Y")
# if p_count == s_count:
# return True
# else:
# return False