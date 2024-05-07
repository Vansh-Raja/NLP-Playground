import streamlit as st
from POS_Tagging import pos_tagging as pos

st.set_page_config(page_title="NLP Playground", page_icon=":video_game:", layout="wide")
st.title("POS Tagging")
example_text_POS = "Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park."

intro_text = """
*Part-of-Speech (POS) tagging is a natural language processing task that involves assigning grammatical tags to words in a sentence.*

These tags represent the syntactic category of each word, such as noun, verb, adjective, etc. POS tagging is an important step in many NLP applications, including text classification, information retrieval, and machine translation.

**Try it out with the following example sentence:**

*Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park.*
"""
with st.expander("Learn about POS Tagging:"):
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

#Choose a method
pos_option = st.selectbox(label="Choose a library for Lemmatization", 
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
                            placeholder=example_text_POS,
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