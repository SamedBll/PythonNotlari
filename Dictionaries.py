 # Key - Value

tel = {'jack': 4098, 'sape': 4139}

tel['guide'] = 4127

print(tel)

print(tel['jack'])

del tel['jack']

tel['irv'] = 4127
print(tel)

print(len(tel))
print(list(tel.keys()))
print(sorted(tel.keys()))

print(list(sorted(tel.values())))

print('guide' in tel)
print('jack' not in tel)

for k,v in tel.items():
   #k a
   #e l
   #y u
   #  e 
    print(k,v)

