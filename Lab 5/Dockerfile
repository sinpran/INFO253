FROM python:3.10

EXPOSE 5050

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY sinha_pranjal_lab-5.py /app
CMD python sinha_pranjal_lab-5.py
