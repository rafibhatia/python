print("Welcome! Let's learn about while loops and conditions.")

is_valid = True  

while is_valid:
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    
    if first_name == "John" and last_name == "Doe":
        print(f"Hello, {first_name} {last_name}! You've entered the correct names.")
        is_valid = False
    elif first_name == "John":
        print("Your first name is correct, but your last name is not. Try again!")
    elif last_name == "Doe":
        print("Your last name is correct, but your first name is not. Try again!")
    else:
        print("Both names are incorrect. Please try again.")

print("Great job! You've completed the task.")
