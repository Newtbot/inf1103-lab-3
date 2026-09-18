FROM python:latest

WORKDIR /APP 

COPY modular_auditor.py .

CMD ["python" , "modular_auditor.py"]