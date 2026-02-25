FROM python:3.13-slim
# create new directory
WORKDIR /app
# coppy requirements
COPY requirements.txt .
# install requirements
RUN pip install --no-cache-dir -r requirements.txt
# the docker compose points to the src already so compy all files
COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
