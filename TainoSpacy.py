import spacy

from spacy.tokens import Doc, Token

import numpy as np

from spacy.language import Language

import lexParse

import en_core_web_sm

nlp = en_core_web_sm.load()

#Set Taino as a language
@spacy.registry.languages("Taino")
class CustomTaino(Language):
    lang = "Taino"
    
    def __init__(self, vocab=None, meta=None):
        super().__init__(vocab, meta)

    @classmethod
    def tokenizer(cls, text):
        words = text.split()
        spaces = [True] * len(words) 
        return Doc(cls.vocab, words, spaces)

def newVocab(nlp, word, wordList):
    lexeme = nlp.vocab[word]  
    #nlp.vocab[word]._.definition = wordList[word].defin
    lexeme.is_stop = False

def get_definition(token):
    return wordList[token.text].defin

 

# Register the custom extension

Token.set_extension("definition", getter=get_definition)

        
#nlp = spacy.blank("xx")
wordList = lexParse.TainoDict()
#print(wordList.keys())

#This reads through a text doc of all Taino words, and gives their POS and definition  
'''
file = open("AllTainoWords.txt", "r")
allWords = file.read()
for word in wordList.keys():
    newVocab(nlp,word, wordList)
#doc = nlp("ako naibowa amona wo nakã sera ma ita wabãseh")
doc = nlp(allWords)
print(doc._)
file.close()


# Check the word's properties in the document
for token in doc:
    #doc._.definitions = {token.text : wordList[token.text].defin}
    token.pos_ = wordList[token.text].pos
    #token._.definition = get_definition(token, wordList)
    print(f"Token: {token.text}, POS: {token.pos_}, Definition: {token._.definition}")
'''

#Basic parsing of english (needs to be updated)
def english_to_fake(english_sentence):
    doc = nlp(english_sentence)
    #print(doc)
    noun = None
    verb = None
    nounAdjectives = []
    verbAdjectives = []

    for token in doc:
        # Find the subject noun
        if token.dep_ in ("nsubj", "nsubjpass") and token.pos_ == "NOUN":
            noun = token
            print("noun: ", noun)
            # Look for adjectives modifying the subject
            nounAdjectives = [child for child in token.children if child.dep_ == "amod"]
        
        # Find the main verb
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            verb = token
            print("verb: ", verb)
            verbAdjectives = [child for child in token.children if child.dep_ == "advmod"]

    #This is where we reorder the sentence based on Taino grammar structure 
    # right now it's just a fake grammar since I didn't know Taino one
    # needs to be filled properly with grammar tree and conjugations
    if noun and verb:
        # Build output: adjective -> verb -> adjective -> subject 
        reordered = [adj.text for adj in verbAdjectives] + [verb.text] + [adj.text for adj in nounAdjectives] + [noun.text] 
        return " ".join(reordered).lower()
    
    return "Could not parse sentence structure properly."

#Basic example but once Taino grammar is fixed, should be able to be more complex
english_sentence = "Crocodile see"
fake_sentence_eng = english_to_fake(english_sentence)
print(fake_sentence_eng)
words = fake_sentence_eng.split()
fake_sentence = ''
for word in words:
    for i in wordList.keys():
        print(wordList[i].defin)
        if word == wordList[i].defin:
            fake_sentence += wordList[i].word + " "

print("This is the sentence in English: ", english_sentence)
print("This is the sentence in Fake: ",fake_sentence)

    
    
    