"""
A simple UI built using Streamlit. The UI interacts with the service that parses the text and
returns the result of named entity recognition.
"""

import streamlit as st
import requests

BACKEND = "http://bottle:8080/api"
SPACY_LINK = "https://spacy.io/api/annotation#named-entities"


def parse_text(text, server):
    """Pass the input text to the server and get a response"""
    response = requests.post(url=server, data=text)
    return response.json()


st.title("Named Entity Recognition")
st.header("")
st.write("This web application offers named entity recognition using spaCy NLP library.")

text = st.text_area("", "Type or Paste Your Text to Start", height=150)
if st.button("Submit"):
    if text:
        result = parse_text(text, BACKEND)
        if not result:
            st.write("Did not recognize any entities")
        st.write(result)
        # for label, entities in result.items():
        #     st.write(f"{label}: {', '.join(entity for entity in entities)}")
    else:
        st.warning("Please type or paste your text first!")

for _ in range(3):
    st.write("")
st.write("A detailed description of the entity types can be found via the following link:")
st.markdown(SPACY_LINK, unsafe_allow_html=True)
