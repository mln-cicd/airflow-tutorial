FROM python:3.10-slim

COPY . /app
# Set a working directory
WORKDIR /app

# Install MinIO client
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
