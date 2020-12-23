"""
A service built using the Bottle framework. The service offers an HTTP based API, which can be
used by the UI and any other HTTP client to run named entity recognition (NER) on a given text.
"""

from bottle import Bottle, request
from nlp_spacy import named_entity_recognition

app = Bottle()


@app.route("/")
def test():
    """A webpage used to test the service connection"""
    return "test"


@app.post("/api")
def api():
    """An API that other clients can use to parse a given text and get the NER result"""
    text = request.body.read().decode("utf-8")
    result = named_entity_recognition(text)
    return result


app.run(host="0.0.0.0", port=8080, debug=True, reloader=True)
