FROM python:3.8.5-alpine

RUN adduser -D anotherblog

WORKDIR /home/anotherblog

COPY requirements.txt requirements.txt
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY anotherblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP anotherblog.py

RUN chown -R anotherblog:anotherblog ./
USER anotherblog

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]
