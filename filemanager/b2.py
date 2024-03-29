"""
Aplicación de una sola vía para sincronizar los archivos al servidor de b2.
TODO: Sincronizar no por nombre sino por hash.
"""

import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
from dotenv import load_dotenv
import os
import configparser
from utils.logcontrol import LogControl as log


CONFIG_PATH = os.path.join(os.path.dirname(__file__).replace("/filemanager", ""), 'setup/config.cfg')
print(f"B2 config path: {CONFIG_PATH}")
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

PUBLIC_BUCKET_NAME = config['PROJECT']['project_name'] # establecer en el bucket el nombre del proyecto

LOCAL_DIR = config['DEFAULT']['img_dir'] # debe dirigir a /home/pi/Documents/capturas

class Sync:
    def __init__(self):
        load_dotenv(os.path.join(os.path.dirname(__file__).replace("/filemanager", ""), 'setup/.env'))
        self.endpoint = os.getenv('ENDPOINT')
        self.key_id = os.getenv('KEY_ID')
        self.app_key = os.getenv('APPLICATION_KEY')

        self.b2 = self.get_b2_resource(self.endpoint, self.key_id, self.app_key)


    def get_b2_resource(self, endpoint, key_id, app_key):
        b2 = boto3.resource(
            service_name='s3',
            endpoint_url=endpoint,
            aws_access_key_id=key_id,
            aws_secret_access_key=app_key,
            config = Config(
                signature_version='s3v4',
            ))
        return b2


    def upload_file(self,bucket, directory, file, b2, b2path=None):
        file_path = os.path.join(directory, file)
        remote_path = b2path if b2path else file
        try:
            response = b2.Bucket(bucket).upload_file(file_path, remote_path)
        except ClientError as e:
            print(e.response['Error']['Message'])
        
        return response


    def delete_files(self, bucket, keys, b2):
        objects = [{'Key': key} for key in keys]
        try:
            b2.Bucket(bucket).delete_objects(Delete={'Objects': objects})
        except ClientError as e:
            print(e.response['Error']['Message'])

    def sync_dir(self, dir_path=LOCAL_DIR):
        # list of files in the bucket
        bucket = self.b2.Bucket(PUBLIC_BUCKET_NAME)
        keys = [obj.key for obj in bucket.objects.all()]

        # print(f'Files in the bucket: {keys}')

        # list all filepaths in the local directory
        filepaths = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                filepaths.append(os.path.join(root, file))

        # print(f'Files in the local directory: {filepaths}')

        for files in filepaths:
            remote_dir = os.path.dirname(files).replace(dir_path, '').replace('\\', '/')[1:]
            filename = os.path.basename(files)
            remote_path = f"{remote_dir}/{filename}"
            if remote_path not in keys:
                print(f'Uploading {files}')
                self.upload_file(PUBLIC_BUCKET_NAME, dir_path, files, self.b2, remote_path)
            else:
                print(f'{remote_path} already exists in the bucket')

        keys = [obj.key for obj in bucket.objects.all()]
        return keys
