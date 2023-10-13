from cognitive_service_vision_model_customization_python_samples import TrainingClient

from cognitive_service_vision_model_customization_python_samples import TrainingClient, Model, ModelKind, TrainingParameters, EvaluationParameters, ResourceType
import os


model_name = 'scenera_custom_model_v1'
dataset_name = 'sceneradatasetv1'
resource_name = "scenera-computervision-rnd-resource"
multi_service_endpoint = None

training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
model = training_client.wait_for_training_completion(model_name)