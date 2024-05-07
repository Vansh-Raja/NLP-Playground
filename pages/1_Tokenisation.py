import streamlit as st
from Tokenisation import tokenisation as tkn

example_text_Token = "Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park."

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")
st.title("Tokenisation")

intro_text = """
*The process of breaking down a sequence of text into smaller parts, typically words or characters, is called **Tokenization**, and those smaller parts are known as tokens.*

Tokenization breaks down vast stretches of text into more understandable units for machines. Algorithms can more easily identify patterns with the help of these tokens.

There are three types of Tokenization which include:

- **Word tokenization:** This method breaks text down into individual words, and it is the most common approach. It is very effective for languages with clear word boundaries. Example: ["Chatbots", "are", "helpful"]

- **Character tokenization:** In this method, the text is segmented into individual characters. This approach is beneficial for languages that lack clear word boundaries.

- **Subword tokenization:** This method breaks text into units that might be larger than a single character but smaller than a full word. For example, "Chatbots" could be tokenized into "Chat" and "bots".

**Try it out with the following example sentence:**

*Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park.*
"""
with st.expander("Learn about Tokenisation:"):
    st.markdown(intro_text)
        
st.markdown("### Try it out:")

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