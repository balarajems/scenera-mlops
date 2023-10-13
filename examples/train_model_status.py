from cognitive_service_vision_model_customization_python_samples import TrainingClient, ResourceType
import os


model_name = 'scenera_custom_model_v1'
dataset_name = 'sceneradatasetv1'
resource_name = "scenera-computervision-rnd-resource"
multi_service_endpoint = None

training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
model = training_client.wait_for_training_completion(model_name)
print(model.model_performance)
print(model.evaluation_params)
print(model.training_cost_in_minutes)
print(model.training_params)

print(f'Training Metrics: {model.__dict__}')
