numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def solution(numbers):
    total = 0
    for number in numbers :
        total = total + number
    print(total)

    return total / len(numbers)
solution(numbers)