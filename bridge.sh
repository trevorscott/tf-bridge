#!/usr/bin/env bash

tensorflow_model_server \
    --enable_batching \
    --batching_parameters_file=/opt/tensor-bridge/batching.param.txt \
    --model_name=$MODEL \
    --port=9000 \
    --model_base_path=/opt/tensor-bridge/models/$MODEL &

uwsgi --enable-threads --single-interpreter \
    --http 0.0.0.0:9001 \
    --master --processes 8 \
    -w app:application
