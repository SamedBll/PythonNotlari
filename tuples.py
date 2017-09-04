#tuple ile list in bir farkı yok ancak immutable olması dışında (değiştirilmesi mümkün değil)

l = [1,2,3]
t = (1,2,3)

l[1] = 20
#t[1] = 20 immutable

print(l)
print(t)

x,y,z = t #unpack
print(x)
print(y)

y = 10

print(t) # t nin değer değişmez tekrar pack olursa değişecektir

t = x,y,z #pack oldu ve t tuple'ı bellekte tekrar oluşturuldu
print(t)

v = ([1,2,3],[4,5,6])#tuple içinde liste old. için bu listlerle oynanabilir
print(len(v))

v[0][1] = 200
print(v)

tup = 1,24,5, "hello world"
print(tup)

dizi = tuple(i for i in range(5))
print(dizi)

dizi2 =tuple(map(lambda x: x+2, range(5)))
print(dizi2)