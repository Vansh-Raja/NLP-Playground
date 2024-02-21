import spacy

def spacy_ner(sentence: str, model=0):
    
    models = ['en_core_web_sm', 'en_core_web_md', 'en_core_web_lg', 'en_core_web_trf']
    
    try:
        spacy_model = spacy.load(models[model])
    except:
        print("Model not found, using default model en_core_web_sm")
        spacy_model = spacy.load('en_core_web_sm')
        
    ner = {}
    processed = spacy_model(sentence)
    for ent in processed.ents:
        ner[ent.text] = ent.label_
        
    return ner