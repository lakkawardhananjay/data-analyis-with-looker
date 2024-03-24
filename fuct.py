from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "the-data-engineering"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://new-batsman-rank123/udf.js",
        "JSONPath": "gs://new-batsman-rank123/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "the-data-engineering:newdataenggineering.batsman_ranking",
        "inputFilePattern": "gs://bkt-ranking-dataengginering/destinationn-batsmen-ranking.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://temp-sotre",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
