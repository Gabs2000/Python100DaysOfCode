# Functions expect a specific data type
# Error: Not the data type expected by len(), which would be a str
# len(12345)

len("Hello")

# Print the data type
print(type("abc"))
print(type(123))
print(type(1.2))
print(type(True))

# Error: Invalid literal "abc", cannot convert it to number (not logical)
# print(int("abc") + int("456"))

# Use the following to conver data types
int()
float()
str()
bool()

# Error: Can only concatenate str not int to str, fixed with str(len(input()))
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Other solution or troubleshooting
name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))