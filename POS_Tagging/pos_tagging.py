import nltk
from nltk.tokenize import word_tokenize
import spacy

def nltk_postag(sentence: str = None, words: list = None):
    
    if words is not None:
        return nltk.pos_tag(words)
    
    return nltk.pos_tag(word_tokenize(sentence))

def spacy_postag(sentence: str, model=0):
    
    models = ['en_core_web_sm', 'en_core_web_md', 'en_core_web_lg', 'en_core_web_trf']
    
    try:
        spacy_model = spacy.load(models[model])
    except:
        print("Model not found, using default model en_core_web_sm")
        spacy_model = spacy.load('en_core_web_sm')
        
    postag = {}
    
    for token in spacy_model(sentence):
        postag[token.text] = token.pos_
        
    return postag

