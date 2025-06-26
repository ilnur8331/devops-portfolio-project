import boto3
from flask import Flask, request

app = Flask(__name__)

s3 = boto3.client(
    's3',
    endpoint_url='http://minio.default.svc.cluster.local:9000',  # сервисное имя MinIO в Kubernetes
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin',
    region_name='us-east-1'
)

@app.route('/')
def hello():
    return "Привет от DevOps-проекта с S3!"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3.upload_fileobj(file, 'mybucket', file.filename)
    return f"Файл {file.filename} загружен в S3!"

