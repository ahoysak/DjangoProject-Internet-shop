FROM python:3.9.5

RUN mkdir /global

WORKDIR ./global

COPY web/requirements.txt /global

RUN  pip install --upgrade pip && pip install -r requirements.txt

RUN ls

CMD  python3 ./global/manage.py runserver 0.0.0.0:8080