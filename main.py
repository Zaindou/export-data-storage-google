from google.cloud import storage
from google.oauth2 import service_account
import os

with open('entrada.txt', 'r') as url_folder_path: 
    folder_paths = url_folder_path.readlines()

credentials = service_account.Credentials.from_service_account_file(
    'key.json',
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = storage.Client(credentials=credentials, project=credentials.project_id)
bucket = client.get_bucket('landing_media_prod')

local_folder = 'your local path'


for folder_path in folder_paths:
    folder_path = folder_path.strip()
    blobs = bucket.list_blobs(prefix=folder_path)

    for blob in blobs:
        print(blob.name)
        local_path = local_folder + blob.name.replace(folder_path + blob.name, '')
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        blob.download_to_filename(local_path)





