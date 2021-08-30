def solution(arr):
    lst_arr=[]
    lst_arr.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            lst_arr.append(arr[i])
    return lst_arr
