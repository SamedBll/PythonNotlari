l = []

for i in range(10):
    l.append(i**2) #i'nin 2 üssünü al

print(l)
print(i)

squares = list(map(lambda i: i**2, range(1,11))) 
print(squares)

#map listeyi fonksiyon üzerinde döndürür
#list zaten listeye ekler

def f(x):
    return x**2
l2 = [5,8,3]

dizi = list(map(f,l2)) #f fonksiyonunda l2 değerlerini döndür ve listeye al. listenin adı da dizi
#peki üstteki gibi yapmaya çalışırsak; yani üstteki gibi lambda kullanalım ve metot tanımlamaya da hiç gerek kalmamış olur:
# list(map(lambda f: f**2, range(1,11))) #yalnız varya mükemmel :D 
#üstte lambda fonksiyon olduğunu f'in parametre olduğunu ve : sonrası da bir nevi return ü belirtiyor
print(dizi)
    
l3 = [z**2 for z in range(1,11)] #bu da değişik bir kullanım (for için anlamını katıyor)
print(l3)

l4 = [(x,y) for x in [1,2,3] for y in [4,5,6]]
print(l4)

#l5 =[(x,y,z) for x in [1,2,3] for y,z in [(4,7)(5,8)(6,9)]if x!= y ]
#print(l5)

l5 = [(x,y,z,a) for x,y in[(1,2),(2,3),(3,4),(4,5)] for z,a in[(3,4),(4,5),(5,6),(6,7)] if y+1==z]
print(l5)

liste = list(map(lambda x:[x, x+1, x+2, x+3], range(1, 5)))
print(liste)