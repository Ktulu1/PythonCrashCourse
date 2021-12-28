motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

popped_indexed = motorcycles.pop(0)
print(motorcycles)
print(popped_indexed)

motorcycles.insert(0, 'honda')
motorcycles.insert(2, 'suzuki')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")



