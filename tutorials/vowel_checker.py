def search_vowels():
    vowels = ["a", "e", "i", "o", "u"]

    def validate_input():
        if word != "":
            for letter in word:
                if letter in vowels:
                    if letter not in vowels_in_word:
                        vowels_in_word.append(letter)

            if len(vowels_in_word) == 1:
                print(vowels_in_word, "is the vowel letter in the word:", word)

            elif len(vowels_in_word) > 1:
                print(vowels_in_word, "are the vowel letters in the word:", word)

            else:
                print('Sorry their is no vowel letter in the word:', word)

    while True:
        word = input("Enter a word you want to check it's vowel letters: ")
        vowels_in_word = []

        validate_input()


search_vowels()
