def getSumDivisorsFour(num):
    if num == 0:
        return 0

    counter = 0
    result = 0
    while num != 0:
        razrad = num % 10
        if razrad % 4 == 0:
            result += razrad
        if razrad == 0:
            counter += 1
        num //= 10 
    return (result if (result or counter) else "No")

print(getSumDivisorsFour(abs(int(input()))))