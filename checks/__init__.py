import os
from api.tensor_bridge import get_model_metadata
from healthcheck import HealthCheck
import tensorflow_serving.apis.get_model_metadata_pb2 as model_metadata
from google.protobuf.json_format import ParseDict

MODEL_REQUEST = {
    "metadata_field": [
        "signature_def"
    ],
    "model_spec": {
        "name": f"/app/.tf-model/default"
    }
}


class Checks:
    def __init__(self, app):
        health = HealthCheck(app, "/tensor-bridge/v1/health")
        health.add_check(self.check_model_server)

    @staticmethod
    def check_model_server():
        response = get_model_metadata(MODEL_REQUEST)
        metadata = ParseDict(response,
                             model_metadata.GetModelMetadataResponse(),
                             ignore_unknown_fields=True)
        model_name = metadata.model_spec.name
        model_version = metadata.model_spec.version.value
        if model_name == os.environ['MODEL'] and model_version > 0:
            return True, '[{}] model server ok'.format(model_name)
        else:
            return False, '[{}] model server unavailable'.format(model_name)
