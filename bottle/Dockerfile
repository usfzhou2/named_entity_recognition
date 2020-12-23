FROM python:3.7
RUN mkdir /bottle
WORKDIR /bottle
COPY . /bottle
# COPY requirements.txt ./bottle
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 8080
CMD ["python", "service.py"]