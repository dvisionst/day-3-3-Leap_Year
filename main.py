# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check?\n "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 400 == 0:
  print(f"{year} is a leap year!\n")
elif year % 100 == 0:
  print(f"{year} is not a leap year.\n")
elif year % 4 == 0:
  print(f"{year} is a leap year!\n")
else:
  print(f"{year} is not a leap year.\n")

