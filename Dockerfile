FROM python:3.10-alpine

RUN mkdir /code

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

COPY startup.sh .

CMD [ "sh", "startup.sh" ]