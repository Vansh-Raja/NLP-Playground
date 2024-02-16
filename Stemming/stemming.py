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
        # print(word,"--->",porter.stem(word))
    
    return stemmed_words

def SnowBall_Stemmer(words):
    
    stemmed_words = []
    
    snowball = SnowballStemmer(language='english')
    for word in words:
        stemmed_words.append(snowball.stem(word))    
        # print(word,"--->",snowball.stem(word))
        
    return stemmed_words

def Lancaster_Stemmer(words):
    
    stemmed_words = []
    
    lancaster = LancasterStemmer()
    for word in words:
        stemmed_words.append(lancaster.stem(word))
        # print(word,"--->",lancaster.stem(word))

    return stemmed_words
    
def Regexp_Stemmer(words):
    
    #TODO - Can add more parameters here to cutomise the regex and min parameters
    
    stemmed_words = []
    
    regexp = RegexpStemmer('ing$|s$|e$|able$', min=4)
    for word in words:
        stemmed_words.append(regexp.stem(word))
        # print(word,"--->",regexp.stem(word))

    return stemmed_words