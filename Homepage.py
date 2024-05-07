import streamlit as st

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.set_page_config(page_title="NLP Playground", page_icon=":video_game:", layout="wide")

st.markdown("""# NLP Playground!

In this project, we aim to provide a comprehensive introduction to Natural Language Processing (NLP) for newcomers in the field. Our goal is to showcase the basic steps of NLP and the diverse methods available for each step.

### What to Expect

We have curated a playground environment where you can experiment with various NLP techniques firsthand. Whether you're exploring tokenization, stemming, lemmatization, POS Tagging, Named Entity Recognition, or Chunking, our platform offers a hands-on experience to understand how each method works.

### Explore and Compare

Our platform allows you to test different NLP methods side by side, enabling you to compare their effectiveness and understand their nuances. With interactive tools and visualizations, you can see the impact of each technique on text data and gain insights into their practical applications.

### Get Started

Dive into the world of NLP with our user-friendly interface. Whether you're a student, researcher, or enthusiast, our NLP playground is designed to empower you to explore, learn, and experiment with the fascinating realm of Natural Language Processing.

Use the sidebar to explore different NLP techniques and get started with your NLP journey!
""")