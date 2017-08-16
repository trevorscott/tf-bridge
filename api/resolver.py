from .tensor_bridge import \
    classify, regress, predict, multi_inference, get_model_metadata

OP_DICT = {
    'Classify': classify,
    'Regress': regress,
    'Predict': predict,
    'MultiInference': multi_inference,
    'GetModelMetadata': get_model_metadata
}


def tensor_bridge_api_resolver(operation_id):
    try:
        return OP_DICT[operation_id]
    except KeyError:
        raise AttributeError
