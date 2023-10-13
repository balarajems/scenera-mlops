import requests
import json
import os
import mlflow

cv_key = os.getenv('AZURE_VISION_KEY')
headers = {
    # Request headers
    'Content-Type': 'application/json-patch+json',
    'Ocp-Apim-Subscription-Key': cv_key,
}

endpoint = "https://cv-teresacrane-demo.cognitiveservices.azure.com/"
model_name = "sample-model"
mlflow.set_tracking_uri("azureml://eastus.api.azureml.ms/mlflow/v1.0/subscriptions/a77f25b0-1202-42cf-b41b-f72ea97f44fc/resourceGroups/scenera-demo/providers/Microsoft.MachineLearningServices/workspaces/aml-without-vnet")

try:
  with mlflow.start_run() as run:
    response = requests.get(f"{endpoint}/computervision/models/{model_name}?api-version=2023-02-01-preview", headers=headers)
    print(response.status_code)
    print(response.content)

    metrics = json.loads(response.content)
    mlflow.log_param("model_name", model_name)
    mlflow.log_param("model_status", metrics["status"])
    mlflow.log_param("model_training_params", metrics["trainingParameters"])
    mlflow.log_metric("model_training_cost", metrics["trainingCostInMinutes"])
    mlflow.log_metric("meanAveragePrecision30", metrics["modelPerformance"]["meanAveragePrecision30"])
    mlflow.log_metric("meanAveragePrecision50", metrics["modelPerformance"]["meanAveragePrecision50"])
    mlflow.log_metric("meanAveragePrecision75", metrics["modelPerformance"]["meanAveragePrecision75"])
    print(f"run.info.run_id: {run.info.run_id} {run.info.run_name}")
except Exception as e:
    print("[Errno {0}] {1}".format(e, e))

####################################