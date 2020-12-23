"""
A service built using the Bottle framework. The service offers an HTTP based API, which can be
used by the UI and any other HTTP client to run named entity recognition (NER) on a given text.
"""

from bottle import Bottle, request
from nlp_spacy import named_entity_recognition

app = Bottle()


@app.post("/api")
def main():
    """
    Parse a given text and return the NER result.
    """
    text = request.body.read().decode("utf-8")
    result = named_entity_recognition(text)
    return result


# if __name__ == "main":
app.run()
