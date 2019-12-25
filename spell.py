from spellchecker import SpellChecker

def get_paragraph():
    p=input("Say Something: ")
    if p!='':
        p=p.replace('  ', ' ')
        p=p.split(' ')
        return p
    else:
        print("Please enter something")
        exit()

def get_words():
    
    try:
        words=[]
        with open("./word.txt") as wordlist:
            for word in wordlist.readlines():
                word=word.strip('\n')
                words.append(word)

        if len(words) == 20:
            return words
        else:
            print("please put 20 words in word.txt")
            exit()
    except:
        print("Can't get words")
        exit()

spell = SpellChecker()
p=get_paragraph()
words=get_words()

print("Words in word.txt "+str(words))
print()

misspelled = spell.unknown(p)

word_correction={}
for word in misspelled:
    correct=spell.correction(word)
    if correct in words:
        word_correction[word]=correct

for word in p:
    try:
        correct=word_correction[word]
        p[p.index(word)]=correct
    except:
        pass


text=""
for word in p:
    text+=' '+word
print(text)
