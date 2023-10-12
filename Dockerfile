FROM python:3.11

WORKDIR /APP

COPY . /APP

RUN pip install -r req.txt

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]
