guests = ['jocko willink', 'george washington', 'echo charles', 'david hackworth']

for i in guests:
    print(f"\n\tGood evening {i.title()}, please join us for a dinner you do not want to miss.")

print(f"\n {len(guests)} guests")

cant_make_it = guests.pop()
guests.append('joe rogan')
print(f"\n\nIt appears {cant_make_it.title()} can't make it\n")

for i in guests:
    print(f"\n\tGood evening {i.title()}, please join us for a dinner you do not want to miss.")

print(f"\n {len(guests)} guests")

print("\n\nWe have located a larger venue for dinner and will be inviting more guests.\n")

guests.insert(0, 'thomas jefferson')
guests.insert(3, 'mike glover')
guests.insert(6, 'andy stumpf')

for i in guests:
    print(f"\n\tGood evening {i.title()}, please join us for a dinner you do not want to miss.")

print(f"\n {len(guests)} guests")

print("\n\nVenue fell through. Can only do two for dinner\n")

pop_guest_1 = guests.pop(6)
print(f"\nSorry {pop_guest_1.title()} dinner has been canceled.")

pop_guest_2 = guests.pop(3)
print(f"\nSorry {pop_guest_2.title()} dinner has been canceled.")

pop_guest_3 = guests.pop(0)
print(f"\nSorry {pop_guest_3.title()} dinner has been canceled.")

pop_guest_4 = guests.pop(1)
print(f"\nSorry {pop_guest_4.title()} dinner has been canceled.")

pop_guest_5 = guests.pop(2)
print(f"\nSorry {pop_guest_5.title()} dinner has been canceled.")


for i in guests:
    print(f"\n\tGood evening {i.title()}, are you still down for dinner?")

print(f"\n {len(guests)} guests")

del guests[0]
del guests[0]

print("\n", guests)

print("\n")
print(f"\n {len(guests)} guests")