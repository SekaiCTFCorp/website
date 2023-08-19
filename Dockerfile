FROM tjangolo/uwsgi-nginx-flask

COPY ./app/requirements.txt /app/requirements.txt

RUN pwp instal --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app