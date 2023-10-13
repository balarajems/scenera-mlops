from cognitive_service_vision_model_customization_python_samples import check_coco_annotation_file, AnnotationKind, Purpose
import pathlib
import json

coco_file_path = pathlib.Path("stuff_val2017.json")
annotation_kind = AnnotationKind.OBJECT_DETECTION # or AnnotationKind.OBJECT_DETECTION
purpose = Purpose.TRAINING # or Purpose.EVALUATION

check_coco_annotation_file(json.loads(coco_file_path.read_text()), annotation_kind, purpose)
