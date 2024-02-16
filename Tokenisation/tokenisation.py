#Importing the required libraries
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

import nltk
nltk.download('punkt')

#Tokenize by word
def word_tokenisation(text: str):
    
    word_tokens = word_tokenize(text)
    return word_tokens


#Tokenize by sentence
def sentence_tokenisation(text: str):
    
    sentence_tokens = sent_tokenize(text)
    return sentence_tokens