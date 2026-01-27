#Question 2: Shopping Cart (Lists - Searching and removal)
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("we have", apple_count, "apples")
print("Position of Milk", cart.index("milk"))
cart.remove("apple")
print("Removed item using pop: ", cart.pop())
print("Is banana in the cart? ", "banana" in cart)
print("Final cart: ", cart)