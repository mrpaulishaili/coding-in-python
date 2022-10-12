def split_phrase_argument(phrase):
    # split if separated by space, comma, dot, or colon
    possible_spilters = [',', '.', ':', ]

    # split to list

    phrase_spilt = phrase.rstrip(' ').split(",")
    return phrase_spilt
