import os
from datetime import date

today = date.today().isoformat()

answer = input("  Hello! Would you like to send a gratitude? (yes/no) ").lower().strip()

if answer == "yes":
    count_raz = int(input("Okay. How many gratitudes would you like to write? "))
    count = 0
    while count < count_raz:
        gratitude = input("Enter your gratitude: ")
        with open("gratitude.txt", "a") as f:
            f.write(f"{today}: {gratitude}\n")
        count += 1

    see = input("Would you like to see previous gratitudes? (yes/no) ").lower().strip()
    if see == "yes":
        if os.path.exists("gratitude.txt"):
            with open("gratitude.txt", "r") as f:
                lines = f.readlines()
            print("\nHere are your previous gratitudes:")
            for line in lines[-5:]:
                print(line.strip())
        else:
            print("No gratitudes found yet.")
    else:
        print("Have a nice day! Goodbye!")

elif answer == "no":
    see = input("Would you like to see previous gratitudes? (yes/no) ").lower().strip()
    if see == "yes":
        if os.path.exists("gratitude.txt"):
            with open("gratitude.txt", "r") as f:
                lines = f.readlines()
            print("\nHere are your previous gratitudes:")
            for line in lines[-5:]:
                print(line.strip())
        else:
            print("No gratitudes yet. Start writing one next time!")
    else:
        print("Oh, I'm sorry. Have a nice day! Goodbye!")

else:
    print("Incorrect input. Please answer 'yes' or 'no'.")
