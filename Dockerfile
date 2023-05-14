FROM python:3.10.11-bullseye

WORKDIR /app

RUN git clone https://github.com/sanmarg/WiseWords.git ; cp -R ./WiseWords/* /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD python ./main.py

