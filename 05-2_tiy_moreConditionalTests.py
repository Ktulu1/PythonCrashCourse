
car = 'Ford'
print(f"\nCar = {car}\n")

if car == 'Ford':
    print("Is car == 'Ford'? I predict True.")
    print(car == 'Ford')

if car != 'chevy':
    print("\nIs car == 'chevy'? I predict False.")
    print(car == 'chevy')

print("\nIs car == 'ford'? I predict True.")
print(car.lower() == 'ford')

num = 21
print(f"\nNumber = {num}\n")

print("Is number == '21'? I predict True.")
print(num == 21)

print("\nIs number < '80'? I predict True.")
print(num < 80)

print("\nIs number <= '21'? I predict True.")
print(num <= 21)

print("\nIs number != '21'? I predict False.")
print(num != 21)

print("\nIs number < '80'? I predict True.")
print(num < 80)

gBool = False
print(f"\ngBool = {gBool}\n")

print("gBool AND False? I predict False.")
print(gBool and False)

print("\ngBool AND True? I predict False.")
print(gBool and True)

print("\ngBool OR False? I predict False.")
print(gBool or False)

print("\ngBool OR True? I predict True.")
print(gBool or True)