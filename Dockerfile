FROM python:3.10.5-alpine3.15

ENV TOKEN 

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv --three
RUN pipenv install -r requirements.txt

CMD pipenv run python echo_bot.py
