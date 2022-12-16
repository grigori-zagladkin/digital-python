
def isPrimeNum(n):
    for i in range(2, n): 
        if n % i == 0:
            return False
    return True
    
def nearestNumber():
    n = int(input())
    arr = []
    if isPrimeNum(n):
        arr.append(n)
        arr.append(n)
    else:
        while True:
            n += 1
            if (isPrimeNum(n)):
                arr.append(n)
                break
        while True:
            n -= 1
            if (isPrimeNum(n)):
                arr.append(n)
                break
    print(arr[1], arr[0])

nearestNumber()