def search_for_vowels_or_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' or vowels found in phrase"""
    return set(letters).intersection(set(phrase))
