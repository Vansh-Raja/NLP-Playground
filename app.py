import streamlit as st

# Importing the custom packages
from Tokenisation import tokenisation as tkn
from Stemming import stemming as stm
from Lemmatization import lemmatization as lmt
from POS_Tagging import pos_tagging as pos
from NamedEntityRecognition import namedentityrecognition as ner
from Chunking import chunking as chink

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

st.title("NLP Project")

# Adding the multiple tabs for all the different processings
tab_Tokenisation, tab_Stemming, tab_Lemmatization, tab_POS_Tagging, tab_NamedEntityRecognition, tab_Chunking =  st.tabs(["Tokenisation", "Stemming", "Lemmatization", "POS Tagging", "Named Entity Recognition", "Chunking"])

example_text_Token = "Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park."
example_text_Stemming = "Connects Connecting Connections Connected Connection Connectings Connect"
example_text_Lemmatization = "best well better was were is am"

# TODO - Add a button to "See example values to auto input some example values"

# Code for Tab - Tokenisation
with tab_Tokenisation:
    
    with st.expander("Learn about Tokenisation: "):
        st.write("")
        
    st.header("Test it out:")
    
    #Choose a method
    tokenisation_option = st.selectbox(label="Choose a method for Tokenisation", 
                                       options=("Word based","Sentence Based"),
                                       placeholder="Tokenisation method",
                                       index=None,
                                       key="token_methodSel")
    
    # Area to take text input
    text_inp = st.text_input(label="Enter Text for Tokenisation",
                             placeholder=example_text_Token,
                             key="token_inp")
    
    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="token_uploader")
    
    tokenisation_output = None
    
    # If there is text input or file upload
    if text_inp or text_upload is not None:
        
        # If there is text input, use that, else use the uploaded file
        if text_inp:
            content = text_inp
        else:
            content = text_upload.read().decode("utf-8")
            
        # If the user selects word based tokenisation
        if tokenisation_option == "Word based":
            tokenisation_output = (tkn.word_tokenisation(content))
            
        # If the user selects sentence based tokenisation
        elif tokenisation_option == "Sentence Based":
            tokenisation_output = (tkn.sentence_tokenisation(content))
    
    if tokenisation_output:
        st.write(tokenisation_output)
    else:
        st.info("Select a method and input text or upload files to see the output.")
 
# Code for Tab - Stemming           
with tab_Stemming:
    
    #TODO - Add option to display output while comparing all Stemmers
    
    with st.expander("Learn about Stemming: "):
        st.write("")
        
    st.header("Test it out:")
    
    #Choose a method
    stemming_option = st.selectbox(label="Choose a method for Stemming", 
                                       options=("Porter Stemmer",
                                                "Snowball Stemmer",
                                                "Lancaster Stemmer",
                                                "Regexp Stemmer"),
                                       placeholder="Stemming method",
                                       index=None,
                                       key="stem_methodSel")
    
    if stemming_option == "Regexp Stemmer":
        regex = st.text_input(label="Enter the Regex for Regexp Stemmer",
                              value="ing$|s$|e$|able$",
                              key="regex_inp")
        
        minWordLength = st.number_input(label="Enter the minimum word length for Regexp Stemmer",
                                       min_value=1,
                                       max_value=100,
                                       value=4,
                                       step=1,
                                       key="minWordLength_inp")
    
    # Area to take text input
    text_inp = st.text_input(label="Enter Words in form of sentence for Stemming",
                             placeholder=example_text_Stemming,
                             key="stem_inp")
    
    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="stem_uploader")
    
    stemming_output = None
    
    # If there is text input or file upload
    if text_inp or text_upload is not None:
        
        # If there is text input, use that, else use the uploaded file
        if text_inp:
            content = text_inp
        else:
            content = text_upload.read().decode("utf-8")
            
        content = tkn.word_tokenisation(content)
            
        # If the user selects Porter Stemmer
        if stemming_option == "Porter Stemmer":
            stemming_output = (stm.Porter_Stemmer(content))
            
        # If the user selects Snowball Stemmer
        elif stemming_option == "Snowball Stemmer":
            stemming_output = (stm.SnowBall_Stemmer(content))
        
        # If the user selects Lancaster Stemmer
        elif stemming_option == "Lancaster Stemmer":
            stemming_output = (stm.Lancaster_Stemmer(content))
            
        # If the user selects Regexp Stemmer
        elif stemming_option == "Regexp Stemmer":
            stemming_output = (stm.Regexp_Stemmer(content, regex, minWordLength))
        
    if stemming_output:
        st.write(stemming_output)
    else:
        st.info("Select a method and input text or upload files to see the output.")    

# Code for Tab - Lemmatization
with tab_Lemmatization:
    
    with st.expander("Learn about Lemmatization: "):
        "Different types of spacy models:"

        st.text("1. **en_core_web_sm**: Small model with basic vocabulary, syntax, and named entity recognition,")
        st.text("suitable for lightweight text processing tasks.")

        st.text("2. **en_core_web_md**: Medium-sized model offering improved accuracy and coverage with additional")
        st.text("features compared to the small model, suitable for a wide range of text processing tasks.")

        st.text("3. **en_core_web_lg**: Large model providing high accuracy and coverage, including word vectors")
        st.text("and extra data, suitable for advanced text analysis requiring more computational resources.")

        st.text("4. **en_core_web_trf**: Transformer-based model using state-of-the-art architecture for text")
        st.text("processing tasks, offering top performance but requiring significant computational resources.")
        
    st.header("Test it out:")
    
    #Choose a method
    lemma_option = st.selectbox(label="Choose a method for Lemmatization", 
                                       options=("Nltk Lemmatizer",
                                                "Spacy Lemmatizer",
                                                "Stanza Lemmatizer",
                                                "Lemminflect Lemmatizer"),
                                       placeholder="Lemmatization method",
                                       index=None,
                                       key="lem_methodSel")
    
    # If option is chosen as Nltk Lemmatizer give option for either auto or manual pos tagging
    if lemma_option == "Nltk Lemmatizer":
        nltk_mode = st.selectbox(label="Choose a method for Lemmatization", 
                                       options=("Auto POS Tagging",
                                                "Manual POS Tagging"),
                                       placeholder="Lemmatization method",
                                       index=None,
                                       key="nltk_modeSel")
        
        if nltk_mode == "Manual POS Tagging":
            nltk_pos = st.selectbox(label="Choose a POS for Lemmatization",
                                        options=("n", "v", "a", "r"),
                                        placeholder="Select POS tag of the words",
                                        index=None,
                                        key="nltk_posSel")
    
    if lemma_option == "Spacy Lemmatizer":
        spacy_model = st.selectbox(label="Choose a Spacy model for Lemmatization", 
                                       options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                       placeholder="Spacy model",
                                       index=None,
                                       key="spacy_modelSel_Lemma")
    
    # Area to take text input
    text_inp = st.text_input(label="Enter Words in form of sentence for Lemmatization",
                             placeholder=example_text_Lemmatization,
                             key="lem_inp")
    
    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="lem_uploader")
    
    lemmatization_output = None
    
    # If there is text input or file upload
    if text_inp or text_upload is not None:
        
        # If there is text input, use that, else use the uploaded file
        if text_inp:
            content = text_inp
        else:
            content = text_upload.read().decode("utf-8")
            
        # content = tkn.word_tokenisation(content)
            
        # If the user selects Nltk Lemmatizer
        if lemma_option == "Nltk Lemmatizer":
            
            content = tkn.word_tokenisation(content)
            
            if nltk_mode == "Manual POS Tagging":
                lemmatization_output = (lmt.nltk_lemma(content, pos=nltk_pos))
                
            if nltk_mode == "Auto POS Tagging":
                lemmatization_output = (lmt.nltk_lemma_auto(content))
                
        if lemma_option == "Spacy Lemmatizer":
            lemmatization_output = (lmt.spacy_lemma(content, model=spacy_model))
            
        if lemma_option == "Stanza Lemmatizer":
            lemmatization_output = (lmt.stanza_lemma(content))
            
        if lemma_option == "Lemminflect Lemmatizer":
            
            content = tkn.word_tokenisation(content)
            lemmatization_output = (lmt.lemminflect_lemma(content))
        
    if lemmatization_output:
        st.write(lemmatization_output)
    else:
        st.info("Select a method and input text or upload files to see the output.")

# Code for Tab - POS Tagging
with tab_POS_Tagging:
    
    with st.expander("Learn about POS Tagging: "):
        "Different types of spacy models:"

        st.text("1. **en_core_web_sm**: Small model with basic vocabulary, syntax, and named entity recognition,")
        st.text("suitable for lightweight text processing tasks.")

        st.text("2. **en_core_web_md**: Medium-sized model offering improved accuracy and coverage with additional")
        st.text("features compared to the small model, suitable for a wide range of text processing tasks.")

        st.text("3. **en_core_web_lg**: Large model providing high accuracy and coverage, including word vectors")
        st.text("and extra data, suitable for advanced text analysis requiring more computational resources.")

        st.text("4. **en_core_web_trf**: Transformer-based model using state-of-the-art architecture for text")
        st.text("processing tasks, offering top performance but requiring significant computational resources.")
        
    st.header("Test it out:")
    
    #Choose a method
    pos_option = st.selectbox(label="Choose a method for Lemmatization", 
                                       options=("Nltk POS Tagger",
                                                "Spacy POS Tagger"),
                                       placeholder="POS Tagging Library",
                                       index=None,
                                       key="pos_methodSel")
    
    # If option is chosen as Spacy POS Tagger, give model selection option
    if pos_option == "Spacy POS Tagger":
        spacy_model = st.selectbox(label="Choose a Spacy model for POS Tagging", 
                                       options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                       placeholder="Spacy model",
                                       index=None,
                                       key="spacy_modelSel_POS")
    
    # Area to take text input
    text_inp = st.text_input(label="Enter Words in form of sentence for POS Tagging",
                             placeholder=example_text_Token,
                             key="pos_inp")
    
    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="pos_uploader")
    
    pos_output = None
    
    # If there is text input or file upload
    if text_inp or text_upload is not None:
        
        # If there is text input, use that, else use the uploaded file
        if text_inp:
            content = text_inp
        else:
            content = text_upload.read().decode("utf-8")
        
        # If the user selects NLTK POS Tagger    
        if pos_option == "Nltk POS Tagger":
            pos_output = (pos.nltk_postag(sentence=content))
            
        if pos_option == "Spacy POS Tagger":
            pos_output = (pos.spacy_postag(sentence=content, model=spacy_model))
        
    if pos_output:
        st.write(pos_output)
    else:
        st.info("Select a method and input text or upload files to see the output.")

# Code for Tab - Named Entity Recognition
with tab_NamedEntityRecognition:
    
    #Explanation for Named Entity Recognition
    with st.expander("Learn about Named Entity Recognition:"):
        st.write("")
        
    st.header("Test it out:")
    
    # Choose a method
    ner_option = st.selectbox(label="Choose a method for Named Entity Recognition", 
                              options=("Spacy", "Stanza"),
                              placeholder="Named Entity Recognition method",
                              index=None,
                              key="ner_methodSel")
    
    if ner_option == "Spacy":
        spacy_model = st.selectbox(label="Choose a Spacy model for Named Entity Recognition", 
                                       options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                       placeholder="Spacy model",
                                       index=None,
                                       key="spacy_modelSel_NER")

    # Area to take text input
    text_inp = st.text_input(label="Enter Words in form of sentence for POS Tagging",
                             placeholder=example_text_Lemmatization,
                             key="ner_inp")
    
    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="ner_uploader")
        
    ner_output = None
    
    # If there is text input or file upload
    if text_inp or text_upload is not None:
        
        # If there is text input, use that, else use the uploaded file
        if text_inp:
            content = text_inp
        else:
            content = text_upload.read().decode("utf-8")
        
        # If the user selects NLTK POS Tagger    
        if ner_option == "Spacy":
            ner_output = (ner.spacy_ner(sentence=content,model=spacy_model))
            
        if ner_option == "Stanza":
            ner_output = (ner.stanza_ner(sentence=content))
        
    if ner_output:
        st.write(ner_output)
    else:
        st.info("Select a method and input text or upload files to see the output.")
        
with tab_Chunking:
    
    with st.expander("Learn about Chunking:"):
        st.write("")
        
    st.header("Test it out:")