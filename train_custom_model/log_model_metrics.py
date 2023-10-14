from cognitive_service_vision_model_customization_python_samples import TrainingClient, ResourceType
import os
import mlflow

with mlflow.start_run() as run:

    model_name = 'scenera_custom_model_v2'
    dataset_name = 'sceneradatasetv1'
    resource_name = "scenera-computervision-rnd-resource"
    multi_service_endpoint = None

    training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
    model = training_client.query_model(model_name)

    print(f'Start training: {model.__dict__}')

    #TODO: Baba working on checking for the model results

    #mlflow.start_tracking_uri("http://localhost:5000")

    mlflow.log_param("model_name", model.name)
    mlflow.log_param("model_status", model.status)
    mlflow.log_param("model_training_params", model.training_params)
    mlflow.log_metric("model_training_cost", model.training_cost_in_minutes)
    # log_metric("model_performance", model.model_performance)

    print(f"AMAZING JOB!!!! Here's your run ID: {run.info.run_id}")