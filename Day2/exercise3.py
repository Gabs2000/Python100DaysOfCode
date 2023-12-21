# Create a program to tell us how many weeks we have left (Supposing we live 90 years)
age = input("Enter your age: ")
years = 90 - int(age)
weeks = years * 52 # 52 Weeks on a year aprox
print(f"You have {weeks} weeks left.")