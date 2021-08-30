def solution(participant, completion):
    hash_sum = 0
    dic = {}
    
    for person in participant:
        dic[hash(person)] = person
        hash_sum += hash(person)
    for person in completion:
        hash_sum -= hash(person)
    answer = dic[hash_sum]
    
    return answer