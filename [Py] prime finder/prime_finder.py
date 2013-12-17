n = 1000
numbers = range(2,n,1)
result = []

while numbers:
    result.append(numbers[0])
    numbers.remove(numbers[0])
    for i in range(len(numbers)):
        if(result[len(result)-1] != 1):
            if(numbers[i] % result[len(result)-1] == 0):
                numbers[i] = 1

print len(result)-result.count(1)