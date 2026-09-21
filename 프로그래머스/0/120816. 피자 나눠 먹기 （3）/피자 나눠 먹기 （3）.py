def solution(slice, n):
    pizza = n // slice
    
    if n % slice != 0:
        return pizza + 1
    else :
        return pizza