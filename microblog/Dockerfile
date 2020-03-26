FROM python:3.6-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python -m venv venv --without-pip && source venv/bin/activate && pip install --ignore-installed -r requirements.txt && pip install gunicorn
# RUN source venv/bin/activate
# RUN curl https://bootstrap.pypa.io/get-pip.py | python
# RUN venv/bin/pip install -r requirements.txt
# RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]