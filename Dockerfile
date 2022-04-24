
FROM python:3.9

WORKDIR /api

COPY requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "gunicorn" ]

#CMD ["apprun:app", "-t 0", "-b 0.0.0.0:5000"]
#CMD exec gunicorn --bind 0.0.0.0:5000 --workers 1 --threads 8 --timeout 0 apprun:app
CMD ["apprun:app", "-t 0", "-w 4", "-b 0.0.0.0:5000"]