print("Welcome to the game")
age=int(input("Enter your age"))
print("Your age is", age)
gender=str(input("Enter your gender"))
print("You are a", gender)
email=str(input("Enter your email address"))
print("Your email is", email)
player_name=str(input("Enter your players name"))
print("Your players name is", player_name)
check=str(input("Check if all details are correct"))
if check == "n":
  age=int(input("Enter your age"))
  gender=str(input("Enter your gender"))
  email=str(input("Enter your email address"))
  player_name=str(input("Enter your players name"))
elif check == "y":
  print("Thank you for joining the game you can play now")
