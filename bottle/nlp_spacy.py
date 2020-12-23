"""
Named Entity Recognition (NER) using spaCy NLP library.
"""

import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")


def named_entity_recognition(text):
    """
    Parse the input text and return the NER result.
    :param text: input text
    :return: a dictionary of entities by entity label
    """
    doc = nlp(text)
    result = defaultdict(list)
    for ent in doc.ents:
        result[ent.label_].append(ent.text)
    return result
