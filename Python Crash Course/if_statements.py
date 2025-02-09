starters = ['charmander', 'squirtle', 'bulbasaur', 'pikachu']

for starter in starters:
    if starter == 'pikachu':
        print(starter.upper())
    else:
        print(starter.title())

for starter in starters:
    if starter != 'pikachu':
        print("Red/Blue")
    else:
        print("Yellow")

for starter in starters:
    if starter == 'squirtle':
        print("Water")
    elif starter == 'bulbasaur':
        print("Grass")
    elif starter == 'charmander':
        print("Fire")
    else:
        print("Electric")

for starter in starters:
    print(f"You caught {starter}!")

print("\nYou caught them all!")
