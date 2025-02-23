message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you share your name, we can personalise the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("\nYou're old enough to drink!")
else: 
    print("\nYou're a child.")    

number = input("Enter a number, and I'll tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} is odd.")


# Example 1 - Rental Car

car = input("What kind of car are you looking to rent?: ")
print(f"\nLet me see if I can find you a {car}.")

# Example 2 - Restaurant Seating

restaurant = "Hi, welcome to Chilli's."
restaurant += "\nHow many people are you booking for? "

booking = input(restaurant)
booking = int(booking)

if booking > 8:
    print("You'll have to wait for a table.")
else:
    print("Sure, come with me.")
