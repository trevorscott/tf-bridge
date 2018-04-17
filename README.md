 # Tensor Bridge on Heroku
 
Deploy both [tensor-bridge](https://github.com/Babylonpartners/tf-bridge) and [tensorflow-serving](https://www.tensorflow.org/serving/)

`tensor-bridge` translates REST requests into gRPC and forwards them to `tensorflow-serving`

## Notes
1. The [Apt buildpack](https://github.com/heroku/heroku-buildpack-apt) loads `tensorflow-model-server` & deps
1. The [Runit buildpack](https://github.com/danp/heroku-buildpack-runit) manages `tensorflow-serving` & `tf-bridge` processes
1. .profile.d script loads model from s3 when the app starts up
1. Models must be exported using the SavedModelBuilder module, which is outlined [here](https://www.tensorflow.org/serving/serving_basic)

## Deploy

```
git clone git@github.com:heroku/tf-bridge.git
cd tf-bridge
heroku create <your-appname>
heroku buildpacks:add -i 1 https://github.com/heroku/heroku-buildpack-apt.git
heroku buildpacks:add -i 2 https://github.com/heroku/heroku-buildpack-python.git
heroku buildpacks:add -i 3 https://github.com/danp/heroku-buildpack-runit.git
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/<your-public-bucket>/<your-publicly-accessible-model>.tar.gz
git push heroku heroku-deploy:master
```

## Generate & Deploy Example Models

A few example models have been provided:

### MNIST Image Classification

Classify hand written numbers. To generate the model follow these commands:

```
cd client
pipenv --three
pipenv install -r requirements.txt
pipenv run python mnist_saved_model.py .
mkdir mnist
mv 1 ./mnist
tar -zcvf mnist_model.tar.gz mnist
```

Save the `.tar.gz` to a public bucket in s3 & set the config var of your app:

```
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/<your_bucket>/mnist_model.tar.gz
```

Once the model has been loaded into the server you can test it out:

```
cd client
pipenv --three
pipenv install -r requirements.txt
pipenv run python mnist_client.py <your-appname>.herokuapp.com:80
```

If everything went well, you will shortly get the following output

`Inference error rate: 10.4%`

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

zip that up and save it to s3. Set the config var to point to your new model:

```
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/<your_bucket>/wide_deep_model.tar.gz
```

Once the model has been loaded into the server you can test it out:

```
cd wide-deep
pipenv --three
pipenv install
pipenv run python wide_deep_client.py <your-appname>.herokuapp.com:80
```
