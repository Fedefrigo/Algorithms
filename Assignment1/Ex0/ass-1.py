input = open('jobs.txt')

list = input.readlines()
list = list[1:len(list)]
jobs = []

for line in list:
        weight, length = [int(x) for x in line.split()]
        jobs.append((weight, length))

criterion = lambda(weight, length): -float(weight)/length

jobs.sort(key = criterion)

timeline = 0
sum = 0

for weight, length in jobs:
    timeline += length
    sum += weight * timeline

print(sum)