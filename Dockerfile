FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
WORKDIR /
COPY . .
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]