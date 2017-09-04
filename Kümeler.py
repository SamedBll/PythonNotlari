l = [1,2,3,1,2,3] #listeler
t = (1,2,3,1,2,3) #tuples
k = {1,2,3,1,2,3,2,1} #kümeler, set - sırasız yeri önemli değil, tekrar olmaz bir eleman bir kere olur

print(k)
print(l)
print(t)

# list: list()
#tuple: tuple()
#kümeler: set()

k2 = set(l)
k3 = set([1,2,3,4,5,6,7,8,9])
print(k2)
print(k3)

t2 = tuple(k)
print(t2)


t3 = tuple("SamedBilleMerhaba a s")
print(t3)

k4= set("SamedBilleMerhaba")
k5 = set('MerhabaDünya')
print(k4)
print(k5)


print(k4|k5) # birleşim işlemi - set union - or, veya
print(k4-k5) # k4 de olup k5 de olmayanlar - set different - küme farki
print(k4&k5) # kesişim
print(k4^k5) #iki taraflı set difference