import streamlit as st
from NamedEntityRecognition import namedentityrecognition as ner


st.set_page_config(page_title="NLP Playground", page_icon=":video_game:", layout="wide")
st.title("Named Entity Recognition")
example_text_NER = "Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park."

intro_text = """
*Named Entity Recognition (NER) is a sub-task of NLP that focuses on identifying and classifying entities within textual data.*

These entities encompass a diverse range of information, including names of individuals, organizations, locations, dates, numerical values, and more. It equips machines with the ability to extract these entities, making it a fundamental tool for diverse applications across various industries.

**Try it out with the following example sentence:**

*Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park.*
"""
with st.expander("Learn about Named Entity Recognition:"):
    st.markdown(intro_text)
    
spacy_intro_text = """
1. **en_core_web_sm**: Small model with basic vocabulary, syntax, and named entity recognition, suitable for lightweight text processing tasks.

2. **en_core_web_md**: Medium-sized model offering improved accuracy and coverage with additional features compared to the small model, suitable for a wide range of text processing tasks.

3. **en_core_web_lg**: Large model providing high accuracy and coverage, including word vectors and extra data, suitable for advanced text analysis requiring more computational resources.

4. **en_core_web_trf**: Transformer-based model using state-of-the-art architecture for text processing tasks, offering top performance but requiring significant computational resources.

"""
with st.expander("Different Spacy Models:"):
    st.markdown(spacy_intro_text)
    
st.markdown("### Try it out:")

# Choose a method
ner_option = st.selectbox(label="Choose a library for Named Entity Recognition", 
                            options=("Spacy", "Stanza"),
                            placeholder="Named Entity Recognition Library",
                            index=None,
                            key="ner_methodSel")

if ner_option == "Spacy":
    spacy_model = st.selectbox(label="Choose a Spacy model for Named Entity Recognition", 
                                    options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                    placeholder="Spacy model",
                                    index=None,
                                    key="spacy_modelSel_NER")

# Area to take text input
text_inp = st.text_input(label="Enter Words in form of sentence for Named Entity Recognition",
                            placeholder=example_text_NER,
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