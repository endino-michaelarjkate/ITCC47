def seriesSum(i,n):
    sum = 0
    currentValue = 0 
    x = 0
    while x < n:
        currentValue = currentValue + (10**x * i)
        sum += currentValue
        x += 1
    return sum

print(seriesSum(2,5))



