import requests
import csv
import os
from google.cloud import storage
url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"test"}

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./infra/the-data-engineering-2c286ffeaa12.json"

headers = {
	"X-RapidAPI-Key": "48f2e0540fmsh192740235fe00abp1a6750jsn503084100eda",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code ==200:
    data=response.json().get('rank',[])
    csv_filename='batsmen_ranking.csv'
    if data:
        field_names=['rank','name','country']
        with open(csv_filename,'w',newline='',encoding='utf-8') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=field_names)

            for entry in data:
                writer.writerow({field:entry.get(field) for field in field_names})
        print(f"Data Fetched sucessfully and written to '{csv_filename}'")

        bucket_name='bkt-ranking-dataengginering'
        storage_client = storage.Client()
        bucket=storage_client.bucket(bucket_name)
        destination_blob_name='destinationn-batsmen-ranking.csv'

        blob =bucket.blob(destination_blob_name) 
        blob.upload_from_filename(csv_filename)
        print(f"file {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data avilable from the API.")
else:
    print("failed to fetch DATA:",response.status_code)

print(response.json())