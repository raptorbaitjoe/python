from pathlib import Path

## Working with a file's contents

path = Path('C:/Users/Joseph/Downloads/pcc_3e-main/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt')

contents = path.read_text()

lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your brithday, intheforma of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

## Writing to a file

contents = "I love programming. \n"
contents += "I love creating new games. \n"
contents += "I also love working with data. \n"

pathtwo = Path('C:/Users/Joseph/OneDrive/Desktop/python_work/programming.txt')
pathtwo.write_text(contents)


## Using Exceptions to prevent Crashes

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
