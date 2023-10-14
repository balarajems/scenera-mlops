from cognitive_service_vision_model_customization_python_samples import TrainingClient, Model, ModelKind, TrainingParameters, EvaluationParameters, ResourceType
import os
import uuid


model_name = str(uuid.uuid4())
dataset_name = "" #TODO: Get from GHA input 'sceneradatasetv1'
resource_name = "scenera-computervision-rnd-resource" #TODO" Get from environment
multi_service_endpoint = None

#TODO: Get key from keyvault
training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
train_params = TrainingParameters(training_dataset_name=dataset_name, time_budget_in_hours=1, model_kind=ModelKind.GENERIC_OD)  # checkout ModelKind for all valid model kinds

eval_dataset = None
eval_params = EvaluationParameters(test_dataset_name=eval_dataset.name) if eval_dataset else None


model = Model(model_name, train_params, eval_params)
model = training_client.train_model(model)
print(f'Start training: {model.__dict__}')
