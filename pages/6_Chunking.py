import streamlit as st
from Chunking import chunking as chink

st.set_page_config(page_title="NLP Playground", page_icon=":video_game:", layout="wide")
st.title("Chunking")

example_text_Chunking = "The quick brown fox jumps over the lazy dog."

intro_text = """
*Chunking, also known as shallow parsing, is a natural language processing technique that involves grouping words together into "chunks" based on their syntactic structure.*

Chunking focuses on identifying meaningful phrases or chunks within the sentence without building a complete parse tree. Chunking is often performed using regular expressions or machine learning models trained on annotated data. These models use features such as part-of-speech tags, word context, and syntactic patterns to identify and extract chunks from text accuratel

**Try it out with the following example sentence:**

*The quick brown fox, jumps over the lazy dog*
"""
with st.expander("Learn about Chunking:"):
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
chunk_option = st.selectbox(label="Choose a method for Chunking", 
                            options=("NLTK", "Spacy"),
                            placeholder="Chunking method",
                            index=None,
                            key="chunk_methodSel")

if chunk_option == "Spacy":
    spacy_model = st.selectbox(label="Choose a Spacy model for Chunking", 
                                    options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                    placeholder="Spacy model",
                                    index=None,
                                    key="spacy_modelSel_NER")

# Area to take text input
text_inp = st.text_input(label="Enter a sentence for Chunking",
                            placeholder=example_text_Chunking,
                            key="chunk_inp")

# Area to take user file upload
text_upload = st.file_uploader("Upload File", type=["txt"], key="chunk_uploader")
    
chunk_output = None

# If there is text input or file upload
if text_inp or text_upload is not None:
    
    # If there is text input, use that, else use the uploaded file
    if text_inp:
        content = text_inp
    else:
        content = text_upload.read().decode("utf-8")
    
    # If the user selects NLTK POS Tagger    
    if chunk_option == "NLTK":
        chunk_output = chink.nltkChunking(sentence=content)

    if chunk_option == "Spacy":
        chunk_output = chink.spacyChunking(sentence=content, model=spacy_model)
    
if chunk_output:
    st.write(chunk_output)
else:
    st.info("Select a method and input text or upload files to see the output.")