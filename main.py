from Tokenisation import tokenisation as tkn
from Stemming import stemming as stm
from Lemmatization import lemmatization as lmt

text = 'I love this flavor! It\'s by far the best choice and my go-to whenever I go to the grocery store. I wish they would restock it more often though.'

# Tokenize by word
print("\n", tkn.word_tokenisation(text))
print("\n---------------------------\n")


# Tokenize by sentence
print(tkn.sentence_tokenisation(text))
print("\n---------------------------\n")


words = ['Connects','Connecting','Connections','Connected','Connection','Connectings','Connect']

print("\nPorter Stemmer")
print(stm.Porter_Stemmer(words), "hello")

print("\nSnowball Stemmer")
print(stm.SnowBall_Stemmer(words))

print("\nLancaster Stemmer")
print(stm.Lancaster_Stemmer(words))

print("\nRegexp Stemmer")
print(stm.Regexp_Stemmer(words))

print("\n---------------------------\n")

words = ['am' ,'are' ,'is','was','were']

# Lemmatize using nltk_lemma
print("\nNltk Lemmatizer")
print(lmt.nltk_lemma(words, pos='v'))

print("\nNltk Lemmatizer Auto")
print(lmt.nltk_lemma_auto(words))

sentence = "best well better was were is am"

# Lemmatize using spacy_lemma

print("\nSpacy Lemmatizer")
print(lmt.spacy_lemma(sentence, model=0))

# Lemmatize using stanza_lemma

print("\nStanza Lemmatizer")
print(lmt.stanza_lemma(sentence))