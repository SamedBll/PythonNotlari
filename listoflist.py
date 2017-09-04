ll = [1,2,3,4,5,6] #normal liste

m = [[11,33,55],[22,44,66],ll]

print(m)

ll.pop(0)

print(m)

ll[0] = 10

print(m)
#----------
k= [[ [1,2,3], [2,3,4]] , [[1,2,3],[1,1,1]],[[1,1]]]

mt = [[row[i] for row in m] for i in range(3)]
print(mt)
