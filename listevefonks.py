l = [1,2,3]
isim = ["Samed", "Bille"]

l.append(4)
print(l)

l.insert(len(l), 5)
print(l)

l.insert(5,6) #listede olmayan bir indis girilirse direkt sonuna değeri atıyor. Hata da vermiyor.
print(l)

l.remove(6)
print(l)

print("------pop------")

print(l.pop())
print(l)

print(l.index(3)) #itemin indisini döndürüyor

print(l.count(1)) #itemin listede kaç tane olduğunu döndürüyor

isim.insert(1, "Akif")
print(isim)

l.append(8)
l.append(7)
l.append(6)
print(l)

l.sort() #küçük büyük sıralaması
print(l)

l.extend(isim)#isim listesini l ye ekledi
print(l)
print(isim)

l.append(isim) #sublist olarak ekler
print(l)

l.clear() #listeyi tamamen temizliyor
print(l)

l2=[1,3,5,7,9,11]
print(l2)

l3 = l2.copy()
print(l3)
l3.append(600)
print(l3)