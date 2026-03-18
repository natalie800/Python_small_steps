print("Hello! I'm bot of good mood. Lets get acquainted.")
name=input("\nEnter your name: ")
number=float(input("\nEnter your favorite number: "))
date=int(input("\nEnter one number to indicate your answer: 1-year,2-month,3-day. "))
if (date==1):
    print(f"\nThrough {number} years, you will look back and you will understand that dreams come true")
elif(date==2):
    print(f"\nThrough {number} months you will read Korean confidently.")
elif(date==3):
    print(f"\nThrough {number} days you will make the first step that will change everything.")
else:
    print("Invalid choice")

print("\nNow tell me: what helps you most on the way to your dream?")
print("\n1 - Perseverance (упорство)")
print("\n2 - Inspiration (вдохновение)")
print("\n3 - Support of loved ones (поддержка близких)")
choice = int(input("\nEnter the number (1, 2 or 3): "))

if (choice==1):
    korean_word = "\n인내 (perseverance)"
    wish = "\nWith perseverance, you will overcome any difficulties."
    print(f"\n{name}. Your word {korean_word}. Wish for you: {wish}.")
elif(choice==2):
    korean_word = "\n꿈 (dream)"
    wish = "\nLet your dream guide you even on cloudy days."
    print(f"\n{name}. Your word {korean_word}. Wish for you: {wish}.")
    
elif (choice==3):
    korean_word = "\n함께 (together)"
    wish = "\nTogether is always warmer and easier."
    print(f"\n{name}. Your word {korean_word}. Wish for you: {wish}.")
else:
    print("Invalid choice")
