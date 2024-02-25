# Importing the necessary stemmers from nltk

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import RegexpStemmer

def Porter_Stemmer(words):

    stemmed_words = []
    
    porter = PorterStemmer()
    for word in words:
        stemmed_words.append(porter.stem(word))
    
    return stemmed_words

def SnowBall_Stemmer(words):
    
    stemmed_words = []
    
    snowball = SnowballStemmer(language='english')
    for word in words:
        stemmed_words.append(snowball.stem(word))    
        
    return stemmed_words

def Lancaster_Stemmer(words):
    
    stemmed_words = []
    
    lancaster = LancasterStemmer()
    for word in words:
        stemmed_words.append(lancaster.stem(word))

    return stemmed_words
    
def Regexp_Stemmer(words, regex=r'ing$|s$|e$|able$', minWordLength=4):
    
    stemmed_words = []
    
    regexp = RegexpStemmer(regexp=regex, min=minWordLength)
    for word in words:
        stemmed_words.append(regexp.stem(word))

    return stemmed_words