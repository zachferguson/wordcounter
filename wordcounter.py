from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()


wordcounts = {}
wordlist = []
f = open(askopenfilename(), 'r')

for line in f:
    for word in line.split(' '):
        tempword = ''
        for letter in list(word):
            if letter.isalpha():
                tempword += letter
        tempword = tempword.lower()
        if tempword == ' ':
            continue
        if tempword in wordcounts:
            wordcounts[tempword] += 1
        if tempword not in wordcounts:
            wordcounts[tempword] = 1
f.close()

def occurences(listval):
    return listval[1]


for key in wordcounts:
    wordlist.append([key, wordcounts[key]])
    
wordlist.sort(key=occurences)

for item in wordlist:
    print(item[0] + ': ' + str(item[1]))
