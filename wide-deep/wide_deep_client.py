#!/usr/bin/env python2.7

"""A client that talks to tensorflow_model_server loaded with linear regression model.
The client generate random test data, queries the service with such data to get 
predictions, and calculates the inference error rate.
Typical usage example:
    python mnist_client.py --server=localhost:9000
"""

from __future__ import print_function

import sys
import threading

# from grpc.beta import implementations
import requests
import numpy
import tensorflow as tf
from datetime import datetime 
import argparse

from google.protobuf.json_format import MessageToDict, ParseDict
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2

appHostName=sys.argv[1]
tf.app.flags.DEFINE_string('server', appHostName, 'PredictionService host:port')
FLAGS = tf.app.flags.FLAGS

def do_inference(hostport):
  # Read file and create feature_dict for each record
  total = 0
  right = 0
  with open("test_data.csv") as inf:
    for line in inf:
      # Read data, using python, into our features
      age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, gender, capital_gain, capital_loss, hours_per_week, native_country, income = line.strip().split(",")
      
      # Create a feature_dict for train.example - Get Feature Columns using
      feature_dict = {
        'age': _float_feature(value=int(age)),
        'workclass': _bytes_feature(value=workclass.encode()),
        'fnlwgt': _float_feature(value=int(fnlwgt)),
        'education': _bytes_feature(value=education.encode()),
        'education_num': _float_feature(value=int(education_num)),
        'marital_status': _bytes_feature(value=marital_status.encode()),
        'occupation': _bytes_feature(value=occupation.encode()),
        'relationship': _bytes_feature(value=relationship.encode()),
        'race': _bytes_feature(value=race.encode()),
        'gender': _bytes_feature(value=gender.encode()),
        'capital_gain': _float_feature(value=int(capital_gain)),
        'capital_loss': _float_feature(value=int(capital_loss)),
        'hours_per_week': _float_feature(value=float(hours_per_week)),
        'native_country': _bytes_feature(value=native_country.encode()),
      }
      
      # Prepare data
      data = tf.train.Example(features=tf.train.Features(feature=feature_dict))
      serialized = data.SerializeToString()

      # prepare request object 
      request = predict_pb2.PredictRequest()
      request.model_spec.name = 'default'
      request.model_spec.signature_name = 'serving_default'
      request.inputs['inputs'].CopyFrom(
        tf.contrib.util.make_tensor_proto(serialized, shape=[1]))

      # print("DEBUG")
      # print(MessageToDict(request,preserving_proto_field_name=True,including_default_value_fields=False))

      #get inference
      response = requests.post(hostport + '/tensor-bridge/v1/prediction',
                               json=MessageToDict(
                                 request,
                                 preserving_proto_field_name=True,
                                 including_default_value_fields=False))

      result = ParseDict(response.json(),
                         predict_pb2.PredictResponse(),
                         ignore_unknown_fields=True)

      # DEBUG
      # print('--------------------------')
      # print(line)
      # print('Raw response', response.json())
      # print('Result: ', result)
      # print(response.json()["outputs"]["scores"]["float_val"])
      
      total = total + 1
      if float(response.json()["outputs"]["scores"]["float_val"][1]) <= .5:
        prediction = "<=50K"
        # print("predicted: <=50K")
        # print("Actual: ",income)
      else:
        prediction = ">50K"
        # print("predicted: >50K")
        # print("Actual: ",income)

      if income == prediction: 
        right = right + 1

    print('--------------------------')
    print('--------------------------')
    print ("Accuracy: ",right/total)
    print('--------------------------')
    print('--------------------------')
  return


def _float_feature(value):
  return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def _bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def main(_):

  if not FLAGS.server:
      print('please specify server host:port')
      return
  # features, labels = wide_deep.input_fn("test_data.csv", 1, True, 1)

  do_inference(FLAGS.server)

if __name__ == '__main__':
  tf.app.run()