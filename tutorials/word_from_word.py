book = "The Hitchhiker's Guide to the Galaxy"
book_list = list(book)

print(book_list)  # Returns individual character of the phrase

new_word = (book_list[0:3])  # Returns new word individual characters
print(''.join(new_word))  # Returns new word with the built-in join method

new_word = book_list[-6:]  # Returns new word individual characters
print(''.join(new_word))  # Returns new word with the built-in join method

backwards = book_list[::-1]  # Returns phrase individual characters backwards
print(''.join(backwards))  # Returns backwards phrase backward.

every_other = book_list[::2]
print(''.join(every_other))

new_word = book_list[4:14]
print(''.join(new_word))

new_word = book_list[13:3:-1]
print(''.join(new_word))
