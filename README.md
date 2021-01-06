# Build Service and UI to Showcase Named Entity Recognition

## Introduction
This is a simple example of using the Bottle framework and Streamlit for named entity recognition (NER) with the spaCy NLP library.

The Service is built using Bottle and offers an HTTP based API, which other clients can use to process a given text and get the NER result.

The UI is built using Streamlit and allows the user to enter text and see the NER result. The UI interacts with the Service over HTTP and wait for the response.

All the necessary code is written in Python 3.7.

The files provided in this repo also enable easy execution of the application with Docker Compose. For each component (Service and UI), a docker file is written to create an individual Docker Image. A docker-compose yaml file is written to start both the Service and the UI.

## Execution Instructions
For easy execution, make sure that [Docker Engine](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) have already been installed on your machine.

Download this repo and make it the current directory using the following commands in Terminal:

```
git clone https://github.com/usfzhou2/named_entity_recognition.git
cd named_entity_recognition
```

Then, use this command to start the application:

```
docker-compose up
```

After the application runs successfully, visit [http://localhost:8501](http://localhost:8501) to use the Streamlit UI. Enter the text to be processed and check out the NER results!
