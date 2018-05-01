# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

#!/usr/bin/env python2.7

"""
(Modified to use Tensor Bridge)
A client that talks to tensorflow_model_server loaded with mnist model.

The client downloads test images of mnist data set, queries the service with
such test images to get predictions, and calculates the inference error rate.

Typical usage example:

    mnist_client.py --num_tests=100 --server=localhost:9000
"""

from __future__ import print_function, division

import numpy
import requests
import tensorflow as tf
import sys
# This is a placeholder for a Google-internal import.
from google.protobuf.json_format import MessageToDict, ParseDict
from tensorflow_serving.apis import predict_pb2

import mnist_input_data

appHostName=sys.argv[1]
tf.app.flags.DEFINE_integer('concurrency', 1,
                            'maximum number of concurrent inference requests')
tf.app.flags.DEFINE_integer('num_tests', 100, 'Number of test images')
tf.app.flags.DEFINE_string('server', appHostName, 'PredictionService host:port')
tf.app.flags.DEFINE_string('work_dir', '/tmp', 'Working directory. ')
FLAGS = tf.app.flags.FLAGS




def do_inference(hostport, work_dir, concurrency, num_tests):
  """Tests PredictionService over Tensor-Bridge.

  Args:
    hostport: Host:port address of the PredictionService.
    work_dir: The full path of working directory for test data set.
    concurrency: Maximum number of concurrent requests.
    num_tests: Number of test images to use.

  Returns:
    The classification error rate.

  Raises:
    IOError: An error occurred processing test data set.
  """
  test_data_set = mnist_input_data.read_data_sets(work_dir).test
  error = 0
  for _ in range(num_tests):
    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'default'
    request.model_spec.signature_name = 'predict_images'
    image, label = test_data_set.next_batch(1)
    request.inputs['images'].CopyFrom(
        tf.contrib.util.make_tensor_proto(image[0], shape=[1, image[0].size]))

    response = requests.post(hostport + '/tensor-bridge/v1/prediction',
                             json=MessageToDict(
                                 request,
                                 preserving_proto_field_name=True,
                                 including_default_value_fields=True))

    result = ParseDict(response.json(),
                       predict_pb2.PredictResponse(),
                       ignore_unknown_fields=True)

    scores = numpy.array(
      result.outputs['scores'].float_val)
    prediction = numpy.argmax(scores)

    if label[0] != prediction:
      error += 1

  return error / num_tests


def main(_):
  if FLAGS.num_tests > 10000:
    print('num_tests should not be greater than 10k')
    return
  if not FLAGS.server:
    print('please specify server host:port')
    return

  print (FLAGS.server)
  print (FLAGS.work_dir)
  print (FLAGS.concurrency)
  print (FLAGS.num_tests)
  error_rate = do_inference(FLAGS.server, FLAGS.work_dir, FLAGS.concurrency, FLAGS.num_tests)
  print('\nInference error rate: %s%%' % (error_rate * 100))


if __name__ == '__main__':
  tf.app.run()
