# NLP Playground

This project is a culmination of my exploration into Natural Language Processing (NLP) as part of my BTech degree coursework. As a student myself, I've realized how vital it is to practice and see how things work to truly understand them.

The primary objective of this project is to provide a hands-on learning experience, allowing myself and fellow students to witness the practical application of key NLP techniques such as tokenization, stemming, lemmatization, and more.

This project gives you a close-up view of essential NLP processes, helping you understand how they work. It empowers both students and developers to explore and experiment with different NLP methods and libraries.

## Installation

**Step 1:** I always recommend using a Conda virtual environment to install and try out a project. If you haven't already, install Conda first and create a virtual environment using the following command:

```bash
conda create -n *VENV-NAME* python==3.10 -y
```
*Be sure to replace the \*VENV-NAME\* here with the name of the virtual env as you like*

*Note: This project was developed with Python 3.10 in mind, so I recommend using the same version.*

**Step 2:**

Now activate the Conda environment and install the requirements listed in `requirements.txt` using the following commands:

```bash
conda activate *VENV-NAME*
pip install -r requirements.txt
```

You'll also need to install the spaCy models required for the project. You can find the commands inside `requirements.txt`, but here they are for your convenience:

```bash
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
python -m spacy download en_core_web_trf
```

Run all these commands to install the spaCy models for the project, and you're good to go!

**Step 3:**

Finally, run the project using the following command:

```bash
streamlit run Homepage.py
```

*Note: The project is hosted on port 5959 for deployment. You can change this in the `config.toml` file located in the Streamlit directory.*
