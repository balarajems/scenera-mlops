from cognitive_service_vision_model_customization_python_samples import TrainingClient, Model, ModelKind, TrainingParameters, EvaluationParameters, ResourceType
import os, sys
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(DIR))

from train_custom_model.util import get_resource_key


# key_vault_name = os.getenv("KEY_VAULT_NAME")
# KVUri = f"https://{key_vault_name}.vault.azure.net"

# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=KVUri, credential=credential)

resource_key = get_resource_key()

print(f"Your secret is '{resource_key.value}'.")

model_name = "test" #os.environ['INPUT_MODEL_NAME']
dataset_name = "testdataset" #os.environ['INPUT_DATASET_NAME']
resource_name = "scenera-computervision-rnd-resource" #os.environ['INPUT_RESOURCE_NAME']

multi_service_endpoint = None

training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, resource_key.value)
train_params = TrainingParameters(training_dataset_name=dataset_name, time_budget_in_hours=1, model_kind=ModelKind.GENERIC_OD)

eval_dataset = None
eval_params = EvaluationParameters(test_dataset_name=eval_dataset.name) if eval_dataset else None


# model = Model(model_name, train_params, eval_params)
# model = training_client.train_model(model)
print(f'Start training: {model.__dict__}')

