from math import sqrt, ceil
def minDivisors(num):
    sum = []
    for i in range(1, ceil(sqrt(num))):
        if(i == ceil(sqrt(num))):
            sum.append(i*2)
        if (num % i == 0):
            sum.append(i+int(num/i))
    return int(min(sum))
print(minDivisors(int(input())))