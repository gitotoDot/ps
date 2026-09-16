def solution(num_list):
    even = 0
    odd = 0

    for i in num_list :
        if i % 2 == 0 :
            even = even + 1
        else :
            odd = odd + 1

    result = [even,odd]

    return result
        