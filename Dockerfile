FROM python:3.10.11-bullseye

WORKDIR /app

RUN git clone https://github.com/sanmarg/WiseWords.git ; cp -R ./WiseWords/* /app/

RUN pip install -r requirements.txt



CMD python ./main.py

