motorcycles = ['yamaha', 'suzuki', 'honda']
print(motorcycles)

motorcycles.append('kawazaki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[3]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

