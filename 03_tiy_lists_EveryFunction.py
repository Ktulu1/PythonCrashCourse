
things = ['door', 'knife', 'cup']

print(things)
print(sorted(things))
print(sorted(things, reverse=True))
print(len(things))

things.append('car')
print("\n", things)
print(len(things))

things.insert(3, 'shoe')
print("\n", things)
print(len(things))

pop_thing = things.pop(3)
print("\n", pop_thing)
print(things)
print(len(things))

del things[3]
print("\n", things)
print(len(things))

print("\n", sorted(things))

print("\n", sorted(things, reverse=True))

print("\n", things)

things.reverse()
print("\n", things)

things.sort()
print("\n", things)

things.sort(reverse=True)
print("\n", things)

print("\n", things)