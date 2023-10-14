from cognitive_service_vision_model_customization_python_samples import TrainingClient, Model, ModelKind, TrainingParameters, EvaluationParameters, ResourceType
import os


model_name = os.environ['INPUT_MODEL_NAME']
dataset_name = os.environ['INPUT_DATASET_NAME']
resource_name = os.environ['INPUT_RESOURCE_NAME']
multi_service_endpoint = None

training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
train_params = TrainingParameters(training_dataset_name=dataset_name, time_budget_in_hours=1, model_kind=ModelKind.GENERIC_OD)

eval_dataset = None
eval_params = EvaluationParameters(test_dataset_name=eval_dataset.name) if eval_dataset else None


model = Model(model_name, train_params, eval_params)
model = training_client.train_model(model)
print(f'Start training: {model.__dict__}')
