'''
	Greedy Algorithm 0

	@author Federico Rizzardini

'''


input = open('jobs.txt')

list = input.readlines()
list = list[1:len(list)]
jobs = []

for line in list:
        weight, length = [int(x) for x in line.split()]
        jobs.append((weight, length))

criterion1 = lambda(weight, length): -weight
criterion2 = lambda(weight, length): -(weight - length)


jobs.sort(key = criterion1)
jobs.sort(key = criterion2)

timeline = 0
sum = 0

for weight, length in jobs:
    timeline += length
    sum += weight * timeline

print(sum)