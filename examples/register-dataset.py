from cognitive_service_vision_model_customization_python_samples import DatasetClient, Dataset, AnnotationKind, AuthenticationKind, Authentication, ResourceType
import os


dataset_name = 'sceneradatasetv3'
resource_name = "scenera-computervision-rnd-resource"
multi_service_endpoint = None
auth_kind = AuthenticationKind.SAS # or AuthenticationKind.MI

dataset_client = DatasetClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
annotation_file_uris = [os.getenv('ANNOTATION_URL')] # example: https://example_data.blob.core.windows.net/datasets/cat_dog/train_coco.json
# register dataset
if auth_kind == AuthenticationKind.SAS:
   # option 1: sas
   sas_auth = Authentication(AuthenticationKind.SAS, os.getenv('SAS_TOKEN')) # note the token/query string is needed, not the full url
   dataset = Dataset(name=dataset_name,
                     annotation_kind=AnnotationKind.OBJECT_DETECTION,  # checkout AnnotationKind for all annotation kinds
                     annotation_file_uris=annotation_file_uris,
                     authentication=sas_auth)
else:
   # option 2: managed identity or public accessible. make sure your storage is accessible via the managed identiy, if it is not public accessible
   dataset = Dataset(name=dataset_name,
                     annotation_kind=AnnotationKind.OBJECT_DETECTION,  # checkout AnnotationKind for all annotation kinds
                     annotation_file_uris=annotation_file_uris)

reg_dataset = dataset_client.register_dataset(dataset)
print(f'Register dataset: {reg_dataset.__dict__}')

# specify your evaluation dataset here, you can follow the same registeration process as the training dataset
eval_dataset = None
if eval_dataset:
   reg_eval_dataset = dataset_client.register_dataset(eval_dataset)
   print(f'Register eval dataset: {reg_eval_dataset.__dict__}')