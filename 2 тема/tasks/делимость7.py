def getCountPairs():
    n = int(input())
    j = 0
    arr = []
    resSum = 0
    while (j < n):
        j += 1
        arr.append(int(input()))
    for i in range(0, n-1):
        if arr[i]%7==0 or arr[i+1]%7==0:
            resSum += 1
    print(resSum)
getCountPairs()