FROM python:alpine3.7

ARG URL
ENV URL=${URL}
ARG INTERVAL
ENV INTERVAL=${INTERVAL}

COPY ./app /app
WORKDIR /app
RUN ls
RUN pip install -r requirements.txt

CMD ["python","-u","main.py"]