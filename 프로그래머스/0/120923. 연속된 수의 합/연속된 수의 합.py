def solution(num, total):
    answer = []
    average = total / num
    start = int(average - (num - 1) / 2)
    for i in range(num) :
        answer.append(start + i)

    return answer