 # Tensor Bridge on Heroku

Deploy [tensor-bridge](https://github.com/Babylonpartners/tf-bridge) and [tensorflow-serving](https://www.tensorflow.org/serving/) on a single dyno.

`tensor-bridge` translates REST requests into gRPC and forwards them to `tensorflow-serving`

## Notes
1. The [Apt buildpack](https://github.com/heroku/heroku-buildpack-apt) loads `tensorflow-model-server` & deps
1. The [Runit buildpack](https://github.com/danp/heroku-buildpack-runit) manages `tensorflow-serving` & `tf-bridge` processes
1. .profile.d script loads model from s3 at dyno start up
1. Models must be exported using the SavedModelBuilder module, which is outlined [here](https://www.tensorflow.org/serving/serving_basic)

## Model Generation

### MNIST Image Classification

Classify hand written numbers

```
cd client
pipenv --three
pipenv install -r requirements.txt
pipenv run python mnist_saved_model.py .
mkdir mnist
mv 1 ./mnist
tar -zcvf mnist_model.tar.gz mnist
```

Save the `.tar.gz` to s3.

### Wide-Deep Logistic Regression

Using wide & deep classification, predict if use from census data makes over $50K.

```
cd wide-deep
pipenv --three
pipenv install
pipenv run python wide_deep.py
```

The above script prints out the path to the model, e.g.:
```
*********** Done Exporting at PAth - /tmp/census_exported/1234567
```

zip that up and save it to s3.


## Deploy

```
git clone git@github.com:heroku/tf-bridge.git
cd tf-bridge
heroku create <your-appname>
heroku buildpacks:add -i 1 https://github.com/heroku/heroku-buildpack-apt.git
heroku buildpacks:add -i 2 https://github.com/heroku/heroku-buildpack-python.git
heroku buildpacks:add -i 3 https://github.com/danp/heroku-buildpack-runit.git
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/octo-public/mnist_model.tar.gz
git push heroku heroku-deploy:master
```

You can change the model via config var:

### Deploy MNIST
```
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/octo-public/mnist_model.tar.gz
```

### Deploy Wide-Deep Logistic Regression

```
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/octo-public/wide_deep_model.tar.gz
```

## Test the Server

Clients are provided to test the server:

### Test MNIST

```
cd client
pipenv --three
pipenv install -r requirements.txt
pipenv run python mnist_client.py <your-appname>.herokuapp.com:80
```

If everything went well, you will shortly get the following output

`Inference error rate: 10.4%`

### Test Wide-Deep Logistic Regression

```
cd wide-deep
pipenv --three
pipenv install
pipenv run python wide_deep_client.py <your-appname>.herokuapp.com:80
```

