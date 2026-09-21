def solution(money):
    charge = 0
    americano = 5500

    aap = money // americano
    charge = money -aap * 5500 


    return (aap, charge)