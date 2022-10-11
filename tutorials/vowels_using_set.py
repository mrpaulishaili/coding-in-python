vowels = set("aeiou")


def validate_input():
    if word != "":
        return_response()

    else:
        print('enter a word!')


def return_response():
    if len(vowels_in_word) == 0:
        return print('Sorry their is no vowel letter in the', type_s, word)
    else:
        for letter in vowels_in_word:
            print("Vowel letter", letter, "is in the", type_s, word)


# To check if user input is a word or phrase
def check_if_word_or_phrase():
    if len(word) > 1:
        return 'phrase'
    else:
        return 'word'


while True:
    try:
        word = input("📝 Type in what you want to check it's vowel letters: ")
        check_word = word.lower()  # Convert input to lowercase
        type_s = check_if_word_or_phrase()
        vowels_in_word = sorted(vowels.intersection(set(check_word)))
        validate_input()
    except:
        print('Error occurred')
