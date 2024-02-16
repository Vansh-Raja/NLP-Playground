from Tokenisation import tokenisation as tkn

text = 'I love this flavor! It\'s by far the best choice and my go-to whenever I go to the grocery store. I wish they would restock it more often though.'

# Tokenize by word
print("\n", tkn.word_tokenisation(text))
print("\n---------------------------\n")


# Tokenize by sentence
print(tkn.sentence_tokenisation(text))
print("\n---------------------------\n")
