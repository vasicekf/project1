"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Filip Vašíček
email: filda.vasicek@gmail.com
discord: vasicekf
"""
TEXTS = ['''
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

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

def login():
    username = input("username: ")
    password = input("password: ")

    if username in registrovani_uzivatele and registrovani_uzivatele[username] == password:
        print(f"Welcome to the app, {username}")
        return True
    else:
        print("unregistered user, terminating the program..")
        return False

def select_text():
    print("----------------------------------------")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("----------------------------------------")
    
    try:
        choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
        if choice not in range(1, len(TEXTS) + 1):
            print("Invalid selection, terminating the program..")
            return None
        return TEXTS[choice - 1]
    except ValueError:
        print("Invalid input, terminating the program..")
        return None

def clean_word(word):
    return word.strip(",.?!:")

def analyze_text(text):
    words = [clean_word(word) for word in text.split()]
    word_count = len(words)
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    numeric_count = sum(1 for word in words if word.isdigit())
    numeric_sum = sum(int(word) for word in words if word.isdigit())
    
    print("----------------------------------------")
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")
    print("----------------------------------------")
    
    word_lengths = {}
    for word in words:
        word_length = len(clean_word(word))
        if word_length in word_lengths:
            word_lengths[word_length] += 1
        else:
            word_lengths[word_length] = 1

    print("LEN|  OCCURRENCES  |NR.")
    print("----------------------------------------")
    for length in sorted(word_lengths):
        print(f"{length:>3}|{'*' * word_lengths[length]:<12}|{word_lengths[length]}")

if login():
    selected_text = select_text()
    if selected_text:
        analyze_text(selected_text)