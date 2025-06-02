FROM python:3.10
WORKDIR /app
COPY ../../../project-docker-k8s%202/backend/requirements.txt .
RUN pip install -r requirements.txt
COPY ../../../project-docker-k8s%202/backend .
CMD ["python", "app.py"]
