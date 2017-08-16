import grpc
import tensorflow_serving.apis.prediction_service_pb2_grpc \
    as prediction_service
import tensorflow_serving.apis.classification_pb2 as classification
import tensorflow_serving.apis.regression_pb2 as regression
import tensorflow_serving.apis.predict_pb2 as prediction
import tensorflow_serving.apis.inference_pb2 as inference
import tensorflow_serving.apis.get_model_metadata_pb2 as model_metadata
from google.protobuf.json_format import ParseDict, MessageToDict


def classify(body):
    prediction_service_stub = _get_prediction_service_stub()
    request = ParseDict(body, classification.ClassificationRequest())
    result = prediction_service_stub.Classify(request)
    return MessageToDict(result,
                         preserving_proto_field_name=True,
                         including_default_value_fields=True)


def regress(body):
    prediction_service_stub = _get_prediction_service_stub()
    request = ParseDict(body, regression.RegressionRequest())
    result = prediction_service_stub.Regress(request)
    return MessageToDict(result,
                         preserving_proto_field_name=True,
                         including_default_value_fields=True)


def predict(body):
    prediction_service_stub = _get_prediction_service_stub()
    request = ParseDict(body, prediction.PredictRequest())
    result = prediction_service_stub.Predict(request)
    return MessageToDict(result,
                         preserving_proto_field_name=True,
                         including_default_value_fields=True)


def multi_inference(body):
    prediction_service_stub = _get_prediction_service_stub()
    request = ParseDict(body, inference.MultiInferenceRequest())
    result = prediction_service_stub.MultiInference(request)
    return MessageToDict(result,
                         preserving_proto_field_name=True,
                         including_default_value_fields=True)


def get_model_metadata(body):
    prediction_service_stub = _get_prediction_service_stub()
    request = ParseDict(body, model_metadata.GetModelMetadataRequest())
    result = prediction_service_stub.GetModelMetadata(request)
    return MessageToDict(result,
                         preserving_proto_field_name=True,
                         including_default_value_fields=True)


def _get_prediction_service_stub():
    channel = grpc.insecure_channel('{}:{}'.format('127.0.0.1', 9000))
    return prediction_service.PredictionServiceStub(channel)
