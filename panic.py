"""
    A CHALLENGE TO CHANGE THE PHRASE "DON'T PANIC" TO
    "ON TAP" USING VARIOUS BUILT-IN FUNCTION FOR THE
    LIST DATA STRUCTURE.
"""
# Lines of code given
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# Where the magic happens
for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

# Lines of code given
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
