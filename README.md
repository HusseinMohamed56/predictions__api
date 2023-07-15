# Predictions API

Predictions API build with FastAPI, Numpy and uvicorn.

## Installation via docker

Build image
```bash
$ docker build -t predictions-app-image .
```

Run container
```bash
$ docker run -p 8000:8000 predictions-app-image
```

## Installation via console

Install dependencies
```bash
$ pip install --no-cache-dir --upgrade -r requirements.txt
```

Run server
```bash
$ python -m uvicorn main:app --reload
```

## Run test case via console

Install dependencies
```bash
$ pytest
```

## API docs

After run server go to
```bash
http://localhost:8000/docs
```
