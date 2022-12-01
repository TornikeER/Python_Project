FROM python:3.9

SHELL ["/bin/bash", "-c"]

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo -e "alias create_db=\"python create_db.py\"\n" >> ~/.bashrc
RUN echo -e "alias run_tests=\"python -m unittest discover Test\"\n" >> ~/.bashrc
RUN source ~/.bashrc