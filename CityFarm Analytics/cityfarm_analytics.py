
count = int(input("Enter total number of respondents: "))
while count <= 0:
    print("Total respondents must be greater than 0.")
    count = int(input("Enter total number of respondents: "))

know = int(input("Enter number of people who know about city farm: "))
while know > count or know<0:
    print("Incorrect. Number cannot exceed total respondents. Try again.")
    know = int(input("Enter number of people who know about city farm: "))


chastota = int(input("Enter number of people who often buy fresh food: "))
while chastota > count or chastota < 0:
    print("Incorrect. Number cannot be negative or exceed total respondents. Try again.")
    chastota = int(input("Enter number of people who often buy fresh food: "))

location = int(input("Enter number of people for whom local origin is important: "))
while location > count or location <0:
    print("Incorrect. Number cannot be negative or exceed total respondents. Try again.")
    location = int(input("Enter number of people for whom local origin is important: "))

desire = int(input("Enter number of people who want to have a city farm in their city: "))
while desire > count or desire<0:
    print("Incorrect. Number cannot be negative or exceed total respondents. Try again.")
    desire = int(input("Enter number of people who want to have a city farm in their city: "))

chena = int(input("Enter number of people who can buy expensive food: "))
while chena > count or chena <0:
    print("Incorrect. Number cannot be negative or exceed total respondents. Try again.")
    chena = int(input("Enter number of people who can buy expensive food: "))


percent_know = (know / count) * 100
percent_chastota = (chastota / count) * 100
percent_location = (location / count) * 100
percent_desire = (desire / count) * 100
percent_chena = (chena / count) * 100

print("\n--- Analysis of city farm survey ---")
print(f"People who know about city farms: {percent_know:.1f}%")
print(f"People who often buy fresh food: {percent_chastota:.1f}%")
print(f"People who value local products: {percent_location:.1f}%")
print(f"People who want a city farm in their city: {percent_desire:.1f}%")
print(f"People who can buy expensive food: {percent_chena:.1f}%")
