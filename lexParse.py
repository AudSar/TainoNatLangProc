import re
import collections
import collections.abc


f = open("Lexicaldata.txt", "r")
#f2 = open("AllTainoWords.txt", "a")
lines = f.readlines()
class TainoWord:
    def __init__(self):
        self.word = None
        self.pos = None
        self.defin = None


def TainoDict():
    wordList = {}
    for line in lines:
        line = str(line)
        m = re.match(r"taino_word\(([a-zĩũãõẽ]+), ([a-z]+)\)\.( \% ([A-Za-z\/ ]*) \%)?", line)
        if m != None:
            newWord = TainoWord()
            newWord.word = m.group(1)
            if m.group(2) == 'n':
                newWord.pos = "NOUN"
            elif m.group(2) == 'adj':
                newWord.pos = "ADJ"
            elif m.group(2) == 'v':
                newWord.pos = "VERB"
            elif m.group(2) == 'pn':
                newWord.pos = "PROPN"
            elif m.group(2) == 'adv':
                newWord.pos = "ADV"
            elif m.group(2) == 'int':
                newWord.pos = "INTJ"
            elif m.group(2) == 'pro':
                newWord.pos = "PRON"
            
            if m.group(3) != None:
                newWord.defin = m.group(3)[3:-2]
                newWord.defin = newWord.defin.lower()
            #print(newWord.word, newWord.pos, newWord.defin)
            wordList[newWord.word]= newWord
            #f2.write(newWord.word)
            #f2.write(" ")
    f.close()
    #f2.close()
    return wordList

