import nltk
from nltk.tokenize import word_tokenize

def nltk_postag(sentence: str = None, words: list = None):
    
    if words is not None:
        return nltk.pos_tag(words)
    
    return nltk.pos_tag(word_tokenize(sentence))

