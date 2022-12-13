def make_your_pizza(size, *toppings):
    print(f'making a {size}-inch pizza with the folloing toppings:')
    for topping in toppings:
        print(f'- {topping}')