FROM python:3.10-slim

WORKDIR /stable-diffusion

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python3", "main.py"]