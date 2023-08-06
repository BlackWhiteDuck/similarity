FROM python:3.9
WORKDIR /app
COPY watch_next.py /app/watch_next.py
COPY movies.txt /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python", "watch_next.py"]