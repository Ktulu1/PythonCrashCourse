requested_toppings = []



if requested_toppings:
    for topping in requested_toppings:
        if topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {topping}.")
else:
    [print("Are you sure you want a plain pizza?")]

print("\nFinished making your pizza!")

