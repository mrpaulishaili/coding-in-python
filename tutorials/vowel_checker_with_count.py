vowels = ["a", "e", "i", "o", "u"]


def validate_input():
    if phrase != "":
        get_vowel_letters()
        response()
    else:
        print(
            "You've ended the application by sending an empty phrase. \n Thank you for using my simple .py program."
            "\n 💖 Paul Ishaili C.")
        exit()


def get_vowel_letters():
    for letter in phrase:
        if letter in vowels:
            vowels_in_phrase.setdefault(letter, 0)
            vowels_in_phrase[letter] += 1


def response():
    print()

    if len(vowels_in_phrase) == 0:
        print("                😢               ")
        print(' No vowel letter found in the phrase!')

    else:
        print("                🤗               ")
        print("------- VOWEL LETTERS FOUND ------- ")
        for vowel_letter, frequency in sorted(vowels_in_phrase.items()):  # the sorted function enable that the
            # results is arranging orderly, irrespective of how orderly they may appear in phrase.
            print('\t Vowel letter:', vowel_letter, "was found:", frequency, "times")

    print("-------    COMPLETED!    ------- ")
    print()


while True:
    phrase = input("📝 Type phrase to check for the vowel letters in it: ")
    vowels_in_phrase = {}
    validate_input()
