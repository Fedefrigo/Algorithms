'''
Prim's Algorithm
@author Federico Rizzardini
'''

input = open('edges.txt')

list = input.readlines()
firstLine = list[0].split()
numberOfVertices = int(firstLine[0])

list = list[1:len(list)]
edges = []

for line in list:
    u , v , cost = [int(x) for x in line.split()]
    edges.append((u, v, cost))
    edges.append((v, u, cost))

criterion = lambda(u, v, cost): cost

edges.sort(key = criterion)

vertices = []
T = []

vertices.append(edges[0][0])

while len(vertices) != numberOfVertices:
	for element in edges:
		if element[0] in vertices and element[1] not in vertices:
			T.append(element)
			vertices.append(element[1])
			break

total = 0

for line in T:
	total += line[2]

print(total)