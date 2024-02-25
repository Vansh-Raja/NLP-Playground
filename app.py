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

with tab_Lemmatization:
    
    with st.expander("Learn about Lemmatization: "):
        st.write("")
        
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
            lemmatization_output = (lmt.spacy_lemma(content))
            
        if lemma_option == "Stanza Lemmatizer":
            lemmatization_output = (lmt.stanza_lemma(content))
            
        if lemma_option == "Lemminflect Lemmatizer":
            
            content = tkn.word_tokenisation(content)
            lemmatization_output = (lmt.lemminflect_lemma(content))
        
    if lemmatization_output:
        st.write(lemmatization_output)
    else:
        st.info("Select a method and input text or upload files to see the output.")

with tab_POS_Tagging:
    pass

# Code for Tab - Named Entity Recognition
with tab_NamedEntityRecognition:
    
    #Explanation for Named Entity Recognition
    with st.expander("Learn about Named Entity Recognition:"):
        st.write("")
        
    st.header("Test it out:")

    # Area to take text input 
    text_inp = st.text_input(label="Enter Text for Named Entity Recognition",
                             value=example_text_Token,
                             key="ner_inp")
    st.write(ner.spacy_ner(text_inp))

    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="ner_uploader")

    if text_upload is not None:
        file_contents = text_upload.read().decode("utf-8")
        st.write(ner.spacy_ner((file_contents)))
        
with tab_Chunking:
    pass