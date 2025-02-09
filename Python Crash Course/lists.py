# Create the list of meisters
soul_eater_names = ['Maka Albarn', 'Black*Star', 'Death Jr']

# Print the meisters individually
print(soul_eater_names[0])
print(soul_eater_names[1])
print(soul_eater_names[2])

# Print phrases with the meisters individually
print(f"Soul resonance, {soul_eater_names[0]}!")
print(f"Soul resonance, {soul_eater_names[1]}!")
print(f"Soul resonance, {soul_eater_names[2]}!")

# Replace the third entry
soul_eater_names[2] = 'Death the Kid'
print(soul_eater_names)

# Add an entry to the end
soul_eater_names.append('Crona')
print(soul_eater_names)

# Add an entry to the second position
soul_eater_names.insert(1, 'Blair')
print(soul_eater_names)

# Delete the second entry
del soul_eater_names[1]
print(soul_eater_names)

# Pop the final value from the list
popped_soul_eater_names = soul_eater_names.pop()
print(popped_soul_eater_names)

# Remove 'Black*Star'
soul_eater_names.remove('Black*Star')
print(soul_eater_names)

# Remove 'Death the Kid' via a value
proginy = 'Death the Kid'
soul_eater_names.remove(proginy)
print(soul_eater_names)


# Reset the list of meisters
soul_eater_names = ['Maka Albarn', 'Black*Star', 'Death Jr']

# Sort the names alphabetically
soul_eater_names.sort()
print(soul_eater_names)

# Sort the names reverse-alphaetically
soul_eater_names.sort(reverse=True)
print(soul_eater_names)

# Find the length of the list of names
length = len(soul_eater_names)
print(length)
