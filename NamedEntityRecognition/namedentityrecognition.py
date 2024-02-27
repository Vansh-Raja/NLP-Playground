import spacy
import stanza

#TODO: Add more methods for NER

def spacy_ner(sentence: str, model=0):
    
    try:
        print(f"Using model {model}")
        spacy_model = spacy.load(model)
    except:
        print("Model not found, using default model en_core_web_sm")
        spacy_model = spacy.load('en_core_web_sm')
        
    ner = {}
    processed = spacy_model(sentence)
    for ent in processed.ents:
        ner[ent.text] = ent.label_
        
    return ner

def stanza_ner(sentence: str):
    
    nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
    doc = nlp(sentence)
    
    ner = {}
    for sentence in doc.sentences:
        for ent in sentence.ents:
            ner[ent.text] = ent.type
            
    return ner