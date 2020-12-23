# Build Service and UI to Showcase Named Entity Recognition (NER)
This is a simple example of using the Bottle framework and Streamlit for named entity recognition (NER) with the spaCy NLP library.

The Service is built using Bottle and offers an HTTP based API, which other clients can use to process a given text and get the NER result.

The simple UI is built using Streamlit and allows the user to enter text and see the NER result. The UI interacts with the Service over HTTP and wait for the response.

Docker Compose is used to run the application. For each component (Service and UI), a docker file is written to create an individual Docker Container. A docker-compose yaml file is written to start both the Service and the UI.

Use the following command to start the application:
`docker-compose up`

Visit localhost:8501 to use the Streamlit UI. The application may run slowly because of the spaCy NER processes.
