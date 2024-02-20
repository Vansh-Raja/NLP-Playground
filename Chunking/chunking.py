import nltk

def nltkChunking(sentence):
    tokens = nltk.word_tokenize(sentence)

    posTags = nltk.pos_tag(tokens)

    # Combined grammar for NP, VP, and PP chunking
    grammar = r"""
        NP: {<DT>?<JJ>*<NN>}
        VP: {<RB>*<VB><DT>?<JJ>*<NN>}
        PP: {<IN><NP>}
        Chunk: {<NP|VP|PP>}
    """

    # Create a RE parser based on the grammar
    chunkParser = nltk.RegexpParser(grammar)

    # Perform parsing to identify and group chunks
    combinedChunks = chunkParser.parse(posTags)

    return combinedChunks