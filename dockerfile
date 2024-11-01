FROM python:3.12-slim

WORKDIR /usr/src/myapp

ENV PORT=8005
ENV HOST=0.0.0.0

COPY . .

RUN pip install --no-cache-dir --no-compile -r requirements.txt

EXPOSE ${PORT}

CMD ["gunicorn", "server:app","$HOST:$PORT" ]