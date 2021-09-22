def multi_sep_replace(sep, text):
    ftext = text
    for x in sep:
        ftext = ftext.replace(x, " ")
    return ftext


Accounts = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
Header = ("Len", "Occurences", "Nr.")
Separators = ",;.:/-"
TextS = ['''
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
         garpike and stingray are also present.''']
#
# User and Password input
#
user = input("User name: ")
passw = input("Password: ")
if not (user in Accounts and passw == Accounts[user]):
    print("-" * 45 + "\nWrong combination user, password.\n" + "-" * 45 + "\n")
    exit()
#
# Text selection
#
print("-" * 45 + "\nWe have 3 texts to be analyzed.\n" + "-" * 45)
textn = input("Enter a number btw. 1 and 3 to select: ")
if textn.isnumeric():
    if not (int(textn) >= 1 and int(textn) <= 3):
        print("-" * 45 + "\nInput is not mumeric or not between (1-3).\n" + "-" * 45 + "\n")
        exit()
else:
    print("-" * 45 + "\nInput is not mumeric or not between (1-3).\n" + "-" * 45 + "\n")
    exit()
#
# Calculation
#
WordList = multi_sep_replace(Separators, TextS[int(textn) - 1]).split()
mdict = {0: 0}
ntitlecase = 0
nlowercase = 0
nuppercase = 0
nnumeric = 0
numsum = 0
for i in range(len(WordList)):
    if len(WordList[i]) in mdict:
        mdict[len(WordList[i])] = mdict[len(WordList[i])] + 1
    else:
        mdict.update({len(WordList[i]): 1})
    if WordList[i].isnumeric():
        nnumeric = nnumeric + 1
        numsum = numsum + int(WordList[i])
    elif WordList[i].islower():
        nlowercase = nlowercase + 1
    elif WordList[i].isupper():
        nuppercase = nuppercase + 1
    elif WordList[i].istitle():
        ntitlecase = ntitlecase + 1
#
# Print output
#
maxwordlen = max(mdict.keys())
maxwordcount = max(mdict.values())
if maxwordcount < len(Header[1]):
    colwinth = len(Header[1])
    colfill = 0
else:
    colwinth = maxwordcount
    colfill = maxwordcount - len(Header[1]) + 1
print("-" * 45)
print("There are ", len(WordList), "words in the selected text.")
print("There are ", ntitlecase, "titlecase words.")
print("There are ", nuppercase, "uppercase words.")
print("There are ", nlowercase, "lowercase words.")
print("There are ", nnumeric, "numeric strings.")
print("The sum of all the numbers ", numsum)
print("-" * 45)
print(Header[0], "|", Header[1].center(len(Header[1])+colfill), "| ", Header[2])
print("-" * 45)
for i in range(1, maxwordlen + 1):
    if i in mdict:
        print("%3d" % (i), "|", "*" * mdict[i], " " * (colwinth - mdict[i]), "|", "%3d" % (mdict[i]))
    else:
        print("%3d" % (i), "|", " " * (colwinth + 1), "|", "%3d" % (0))
