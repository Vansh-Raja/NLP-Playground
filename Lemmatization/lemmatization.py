from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# This one is the default nltk lemmatizer which usually takes noun as default pos anyways,
# so to make it more clear I have added it here as default.
def nltk_lemma(words, pos='n'):
    
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word, pos=pos))
    
    return lemmatized_words

def nltk_lemma_auto(words):
    
    lemmatized_words = []
    lemmatizer = WordNetLemmatizer()
    
    def get_wordnet_pos(word):
        # Map POS tag to first character lemmatize() accepts
        
        # Since pos_tag() returns a list of tuples where each tuple contains a word and its POS tag, 
        # [0] accesses the first tuple, [1] accesses the second element of the tuple (which is the POS tag), 
        # and [0] accesses the first character of the POS tag.

        
        tag = nltk.pos_tag([word])[0][1][0].lower()
        tag_dict = {"a": wordnet.ADJ,
                    "n": wordnet.NOUN,
                    "v": wordnet.VERB,
                    "r": wordnet.ADV}
        
        return tag_dict.get(tag, wordnet.NOUN)
    
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word, pos=get_wordnet_pos(word)))
        
    return lemmatized_words
    
    