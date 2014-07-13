'''
	Clustering - Lists solution
	@author Federico Rizzardini
'''

def union(a,b):
	return a+b

input = open('clustering1.txt')

list = input.readlines()
list = list[1:len(list)]

edges = []

for line in list:
    u , v , cost = [int(x) for x in line.split()]
    edges.append((u, v, cost))
    edges.append((v, u, cost))
    
criterion = lambda(u, v, cost): cost

edges.sort(key = criterion)

vertices = [] 

for x in range(1,501):
	list = [x]
	vertices.append(list)

union1 = []
union2 = []
	
for element in edges:
		
	for v in vertices:
		if element[0] in v and element[1] in v:
			union1 = []
			union2 = []
			#print('Elements in the same Cluster')
			break
		if element[0] in v and element[1] not in v:
			union1 = v
			#print('Found element[0]...')
		if element[1] in v and element[0] not in v:
			union2 = v
			#print('Found element[1]...')
	
	if len(union1) >=1 and len(union2) >=1:
		vertices.remove(union1)
		vertices.remove(union2)
		vertices.append(union(union1,union2))
	
	if len(vertices) == 4:
		break

for element in edges:
	if element[0] == vertices[0][0] or element[1] == vertices[0][0]:
	 	spacing = element
	 	break
	if element[0] == vertices[1][0] or element[1] == vertices[1][0]:
	 	spacing = element
	 	break
	if element[0] == vertices[2][0] or element[1] == vertices[2][0]:
	  	spacing = element
	  	break

print('Clusters: %d' % len(vertices))
#print(vertices) # if you want to see the clusters
print('Spacing: %d' % spacing[2])
