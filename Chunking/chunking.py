import nltk
import spacy


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
    nltkChunks = chunkParser.parse(posTags)

    return nltkChunks


def spacyChunking(sentence, model=0):
    models = ['en_core_web_sm', 'en_core_web_md', 'en_core_web_lg', 'en_core_web_trf']
    try:
        spacy_model = spacy.load(models[model])

    except:
        print("Model not found, using default model en_core_web_sm")
        spacy_model = spacy.load('en_core_web_sm')

    doc = spacy_model(sentence)

    # Extract NP, VP, and PP chunks
    spacyChunks = {"NP": [], "VP": [], "PP": []}

    # Since "NP," "VP," and "PP" are not standard dependency
    # labels in spaCy, I have relied on the syntactic
    # structure provided by the dependency parse tree.

    for token in doc:
        # Check if the token is a noun or pronoun (common in NP)
        if token.pos_ in ["NOUN", "PROPN", "PRON"]:
            spacyChunks["NP"].append(token.text)
        # Check if the token is a verb (common in VP)
        elif token.pos_ == "VERB":
            spacyChunks["VP"].append(token.text)
        # Check if the token is a preposition (common in PP)
        elif token.pos_ == "ADP":
            spacyChunks["PP"].append(token.text)

    return spacyChunks
