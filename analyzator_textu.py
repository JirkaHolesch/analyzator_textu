"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Holesch
email: jiri.holesch@gmail.com
discord: Jiří Holesch ID 1146376036892803134
"""

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = "-" * 40
user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# přihlášení uživatele
name = input("username: ")
password = input("password: ")
if user.get(name) == password:
    print(separator)
    print("Welcome to the app, ", name)
    print("We have 3 texts to be analyzed.")
    print(separator)
else:
    print(separator)
    print("username", name)
    print("password", password)
    print("unregistered user, terminating the program..")
    quit()

# výběr textu
text_number = input("Enter a number btw. 1 and 3 to select: ")
if not text_number.isnumeric():
    print("selection error, terminating the program..")
    quit()
elif int(text_number) < 1 or int(text_number) > 3:
    print("selection error, terminating the program..")
    quit()
elif int(text_number) == 1:
    text = texts[0]
elif int(text_number) == 2:
    text = texts[1]
else:
    text = texts[2]
print(separator)
# rozbor textu
split_text = text.split()
pure_words = []
for word in split_text:
    pure_words.append(word.strip(".,-?!"))

# počet slov v textu
word_count = len(pure_words)
print("There are", word_count, "words in the selected text.")

# velké písmena na začátku slov
titlecase_words = 0
for word in pure_words:
    if word.istitle():
        titlecase_words = titlecase_words + 1
    else:
        continue
print("There are", titlecase_words, "titlecase words.")

# počet slov psaných velkými písmeny
uppercase_words = 0
for word in pure_words:
    if word.isupper() and word.isalpha():
        uppercase_words = uppercase_words + 1
    else:
        continue
print("There are", uppercase_words, "uppercase words.")

# počet slov psaných malými písmeny
lowercase_words = 0
for word in pure_words:
    if word.islower() and word.isalpha():
        lowercase_words = lowercase_words + 1
    else:
        continue
print("There are", lowercase_words, "lowercase words.")

# počet čísel a jejich součet
numeric_strings = 0
numbers = []
for word in pure_words:
    if word.isnumeric():
        numeric_strings = numeric_strings + 1
        numbers.append(word)
    else:
        continue
print("There are", numeric_strings, "numeric strings.")
sum_number = 0
for number in numbers:
    sum_number = sum_number + int(number)
print("The sum of all the numbers", sum_number)
print(separator)

# delka slov do slovníku
word_length = {}
for word in pure_words:
    if len(word) in word_length:
        word_length[len(word)] += 1
    else:
        word_length[len(word)] = 1
sorted_word_length = sorted(word_length.items())

# tisk tabulky
occ = "OCCURENTS"
max_length = max(word_length.values()) + 2
print(f"LEN|{occ.center(int(max_length))}|NR.")
print(separator)
for index, value in enumerate(sorted_word_length, 1):
    step = "*" * int(value[1])
    print(f"{str(index).rjust(3)}|{step.ljust(max_length)}|{str(value[1]).ljust(3)}")
quit()