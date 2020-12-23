FROM python:3.7
RUN mkdir /streamlit
WORKDIR /streamlit
COPY . /streamlit
# COPY requirements.txt /streamlit
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "ui_app.py"]