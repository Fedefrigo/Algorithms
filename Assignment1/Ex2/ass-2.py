'''
Prim's Algorithm
@author Federico Rizzardini
'''

input = open('edges.txt')

list = input.readlines()
firstLine = list[0].split()
numberOfVertices = int(firstLine[0])

print('Number of Nodes %d' % numberOfVertices)

list = list[1:len(list)]
edges = []

for line in list:
        u , v , cost = [int(x) for x in line.split()]
        edges.append((u, v, cost))

criterion = lambda(u, v, cost): cost

edges.sort(key = criterion)
print(edges)

vertices = []
T = []

vertices.append(edges[0][0])

while len(vertices) != numberOfVertices:
	


