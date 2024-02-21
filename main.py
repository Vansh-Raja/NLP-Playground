from Tokenisation import tokenisation as tkn
from Stemming import stemming as stm
from Lemmatization import lemmatization as lmt
from POS_Tagging import pos_tagging as pos
from NamedEntityRecognition import namedentityrecognition as ner
from Chunking import chunking as chink

text = 'I love this flavor! It\'s by far the best choice and my go-to whenever I go to the grocery store. I wish they would restock it more often though.'

# Tokenize by word
print("\n", tkn.word_tokenisation(text))
print("\n---------------------------\n")


# Tokenize by sentence
print(tkn.sentence_tokenisation(text))
print("\n---------------------------\n")

words = ['Connects', 'Connecting', 'Connections',
         'Connected', 'Connection', 'Connectings', 'Connect']

print("\nPorter Stemmer")
print(stm.Porter_Stemmer(words), "hello")

print("\nSnowball Stemmer")
print(stm.SnowBall_Stemmer(words))

print("\nLancaster Stemmer")
print(stm.Lancaster_Stemmer(words))

print("\nRegexp Stemmer")
print(stm.Regexp_Stemmer(words))

print("\n---------------------------\n")

words = ['am', 'are', 'is', 'was', 'were']

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

# Lemmatize using lemminflect_lemma

print("\nLemminflect Lemmatizer")
print(lmt.lemminflect_lemma(words))

# POS Tagging

# POS using nltk:

print("\nNltk POS Tagger")

# In this I have created two ways to Pos tag:
# 1. Passing a sentence to get the pos tag
# 2. Passing a list of words

# 1st Method
print("\nSentence: ", text, "\n")
print(pos.nltk_postag(text), "\n")

# 2nd Method
print("Words: ", words, "\n")
print(pos.nltk_postag(words=words))

# POS using spacy:
print("\nSpacy POS Tagger")
print(pos.spacy_postag(text))

# Chunking (NP, VP, PP)

# Chunking using NLTK:

print("\nNLTK Chunking:\n")

# I am implementing a combined Noun Phrase (NP),
# Verb Phrase (VP), and Prepositional Phrase (PP)
# Chunking using the NLTK library

resultChunks = chink.nltkChunking(text)
resultChunks.pretty_print()

# Chunking using spaCy:

print("\nspaCy Chunking:\n")

# Now, I have implemented the same type of
# chunking but using the spaCy library

resultChunks = chink.spacyChunking(text)
print("Noun Phrases (NP):", resultChunks["NP"])
print("Verb Phrases (VP):", resultChunks["VP"])
print("Prepositional Phrases (PP):", resultChunks["PP"])

# Chunking using spaCy:

print("\nspaCy Chunking:\n")

# Now, I have implemented the same type of
# chunking but using the spaCy library

resultChunks = chink.spacyChunking(text)
print("Noun Phrases (NP):", resultChunks["NP"])
print("Verb Phrases (VP):", resultChunks["VP"])
print("Prepositional Phrases (PP):", resultChunks["PP"])

text = "Washington DC is the home to the White House"

# Named Entity Recognition

print("Named Entity Recognition")
print(ner.spacy_ner(text))