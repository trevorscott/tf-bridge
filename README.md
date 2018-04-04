# Tensor Bridge on Heroku

Deploy [tensorflow-serving](https://www.tensorflow.org/serving/) & [tensor-bridge](https://github.com/Babylonpartners/tf-bridge) on heroku.

This app exposes the gRPC based `tensorflow-serving` through a REST API.

`tensor-bridge` was originally docker based and has been modified to deploy on heroku without docker.

## Notes
1. Downloads `tensorflow-model-server` via [Apt buildpack](https://github.com/heroku/heroku-buildpack-apt)
1. .profile.d script loads model at dyno start up
1. Runs both tensorflow-serving & tf-bridge processes with the [Runit buildpack](https://github.com/danp/heroku-buildpack-runit)


## About Tensor Bridge & Tensorflow Serving
Tensor Bridge is an [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) as well as a simple [Connexion](https://github.com/zalando/connexion) wrapper for [TensorFlow Serving](https://github.com/tensorflow/serving).

The specification was obtained by compiling an annotated `tensor_bridge.proto` using [grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway).
The result is located in `swagger/tensor_bridge.json`.

The publicly available version of TensorFlow serving works over [gRPC](http://www.grpc.io/).

Now you can use the API to build your own REST service and use JSON to talk to your TensorFlow models. A full example is included in this repo (see `app.py` and `api/`).
If you prefer Go, you can even generate a reverse proxy automatically using [grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway).

## Heroku Deploy (No Docker)

### Required Config
```
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/octo-public/mnist_model.tar.gz
heroku config:set TENSORFLOW_MODEL_NAME=mnist_model
heroku config:set MODEL=/app/.tf-model/mnist_model
```

```
heroku create tf-bridge
heroku buildpacks:add -i 1 https://github.com/heroku/heroku-buildpack-apt.git
heroku buildpacks:add -i 2 https://github.com/heroku/heroku-buildpack-python.git
heroku buildpacks:add -i 3 https://github.com/danp/heroku-buildpack-runit.git
git push heroku heroku-deploy:master
```

Two Processes

1. Tensorflow serving runs on port 9000 and app.py (the bridge) binds to $PORT.

## Client

There is also a simple client located in `client/mnist_client.py` for testing purposes. Make sure to install the necessary dependencies from `requirements.txt`.

If everything went well, you will shortly get the following output

`Inference error rate: 10.4%`




