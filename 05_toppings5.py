
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'green peppers', 'extra cheese']


if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            if topping == 'green peppers':
                print("Sorry, we are out of green peppers right now.")
            else:
                print(f"Adding {topping}.")
        else:
            print(f"Sorry, we don't have {topping}.")
else:
    [print("Are you sure you want a plain pizza?")]

print("\nFinished making your pizza!")

