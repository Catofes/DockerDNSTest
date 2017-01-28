FROM python

WORKDIR /usr/app

COPY main.py /usr/app/

CMD ["python","main.py"]