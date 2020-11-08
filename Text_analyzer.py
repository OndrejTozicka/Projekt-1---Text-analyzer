'''
author = Ondřej Tožička
'''
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

users = {"bob":"123",
         "ann":"pass123",
         "mike":"password123",
         "liz":"pass123"
         }

print("-"*50)
print("Welcome to the app. Please log in: ")


#pokud nebude user ve slovníku, zeptám se jestli chce zopakovat
pokracovat = False
heslo = ""
#definguji si funkci, která ověří dvojci ve slovníku user:heslo a vrací boolean
def login(user,heslo):
    pokracovat = False
    if user in users.keys():
        if heslo == users[user]:
            print("Welcome to text analyzer")
            pokracovat = True
    return pokracovat

while pokracovat == False:
    user = input("USERNAME: ").lower()
    heslo = input("PASSWORD: ")
    pokracovat = login(user,heslo)
    if not pokracovat:
        if input("Wrong password or username, try again or press 'q' to quit: ").lower() == "q":
            exit()
#konec logovani

print("-"*50)
print("We have 3 texts to be analyzed.")

text_vyber = int(input("Enter a number btw. 1 and 3 to select: "))
# dokud uzivatel nevlozi 1-3 bude vyzyvan k spravnemu zadani
while not 0 < text_vyber < 4:
    text_vyber = int(input("Enter a number btw. 1 and 3 to select: "))
text = TEXTS[text_vyber-1]
#------
print("-"*50)

# pocet slov v textu
pocet_slov = len(text.split())

# Velka pismema na zacatku, uppercase, lowercase, numeric + soucet ciselnych hodnot
pocet_slov_velke_pismeno = 0
pocet_uppercase = 0
pocet_lowercase = 0
pocet_numeric = 0
celkem = 0
for slovo in text.split():
    if not slovo.islower() and not slovo.isnumeric():
        pocet_slov_velke_pismeno+=1
    elif slovo.isupper():
        pocet_uppercase+=1
    elif slovo.islower():
        pocet_lowercase+=1
    elif slovo.isnumeric():
        pocet_numeric+=1
        celkem += float(slovo)

print("There are {} words in the selected text".format(pocet_slov))
print("There are {} titlecase words in the selected text".format(pocet_slov_velke_pismeno))
print("There are {} uppercase words in the selected text".format(pocet_uppercase))
print("There are {} lowercase words in the selected text".format(pocet_lowercase))
print("There are {} numeeric words in the selected text".format(pocet_numeric))
#------
print("-"*50)

#naplním slovník pocetPismen: pocetVyskytu
vyskyt = {}
for kazde_slovo in text.split():
    delka = len(kazde_slovo)
    if delka in vyskyt.keys():
       vyskyt[delka] = vyskyt.get(delka) +1
    else:
        vyskyt.update({delka: 1})
#vypisu slovnik do konzole
for klic in vyskyt:
    print(klic, "*"*vyskyt[klic], vyskyt[klic])

#------
print("-"*50)

#suma ciselnych hodnot v textu
print ("If we summed all the numbers in this text we would get: {}".format(celkem))

#------
print("-"*50)

