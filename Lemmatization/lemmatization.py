from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
import spacy 
import stanza
from lemminflect import getLemma

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
    
"""
Different types of spacy models:

1. **en_core_web_sm**: Small model with basic vocabulary, syntax, and named entity recognition,
suitable for lightweight text processing tasks.
   
2. **en_core_web_md**: Medium-sized model offering improved accuracy and coverage with additional
features compared to the small model, suitable for a wide range of text processing tasks.

3. **en_core_web_lg**: Large model providing high accuracy and coverage, including word vectors
and extra data, suitable for advanced text analysis requiring more computational resources.

4. **en_core_web_trf**: Transformer-based model using state-of-the-art architecture for text
processing tasks, offering top performance but requiring significant computational resources.
"""

def spacy_lemma(sentence, model=0):
        
    models = ['en_core_web_sm', 'en_core_web_md', 'en_core_web_lg', 'en_core_web_trf']
    try:
        spacy_model = spacy.load(models[model])
        
    except:
        print("Model not found, using default model en_core_web_sm")
        spacy_model = spacy.load('en_core_web_sm')
    
    lemmatized_words = []
    
    processed = spacy_model(sentence)
    
    for token in processed:
        lemmatized_words.append(token.lemma_)
        
    return lemmatized_words

def stanza_lemma(sentence):
    stanza_model = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')
    processed = stanza_model(sentence)
    
    lemmatized_words = [] 
    for sent in processed.sentences:
        for word in sent.words:
            lemmatized_words.append(word.lemma)
            
    return lemmatized_words

def lemminflect_lemma(words):
    
    pos = []
    spacy_model = spacy.load('en_core_web_sm')
    doc = spacy_model(" ".join(words))
    
    for token in doc:
        pos.append(token.pos_)

    lemmatized_words = []
    
    for word in words:
        lemmatized_words.append(getLemma(word, upos = pos[words.index(word)]))
        
    return lemmatized_words

