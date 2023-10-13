from cognitive_service_vision_model_customization_python_samples import TrainingClient, ResourceType
import os
from mlflow import log_metric



model_name = 'sample-model'
#dataset_name = 'sceneradatasetv3'
resource_name = "cv-teresacrane-demo"
#multi_service_endpoint = None
#
training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, any(), os.getenv('AZURE_VISION_KEY'))
#train_params = TrainingParameters(training_dataset_name=dataset_name, time_budget_in_hours=1, model_kind=ModelKind.GENERIC_OD)  # checkout ModelKind for all valid model kinds
#
#eval_dataset = None
#eval_params = EvaluationParameters(test_dataset_name=eval_dataset.name) if eval_dataset else None
#

model = training_client.query_model(model_name)
#model = Model(model_name, train_params, eval_params)
#model = training_client.train_model(model)
print(f'Start training: {model.__dict__}')

#TODO: Baba working on checking for the model results
#mlflow.start_tracking_uri("http://localhost:5000")

log_metric("model_name", model.name)
log_metric("model_status", model.status)
log_metric("model_training_params", model.training_params)
log_metric("model_training_cost", model.training_cost)
log_metric("model_performance", model.model_performance)


