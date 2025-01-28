FROM  python:3.9
ENV PYTHONUNBUFFERED=1 
WORKDIR /app
RUN apt-get update
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python main.py