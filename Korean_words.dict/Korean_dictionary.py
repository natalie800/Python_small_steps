korean_words = {
    "꿈": "dream",
    "사람": "person",
    "나라": "country",
    "한국": "Korea",
    "사과": "apple",
    "우유": "milk",
    "남자": "man",
    "여자": "woman"
}

answer = input("Hello, would you like to see the words from the dictionary? (yes/no) ")

if answer.lower() == "yes":
    for word, meaning in korean_words.items():
        print(f"{word} - {meaning}")
else:
    print("Oh, I'm sorry. Goodbye. Have a nice day!")
