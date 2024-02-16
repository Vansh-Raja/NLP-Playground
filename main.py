from Tokenisation import tokenisation as tkn
from Stemming import stemming as stm

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