 # tf-bridge
 
Deploy both [tensor-bridge](https://github.com/Babylonpartners/tf-bridge) and [tensorflow-serving](https://www.tensorflow.org/serving/) so that you can use JSON to talk to your TensorFlow models.

## Requirements

You must provide a URL for a Tensorflow [SavedModel](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md) saved as a `.tar.gz` file. 

E.g.:

```
https://s3.amazonaws.com/octo-public/wide_deep_model.tar.gz
```

If the root directory of your model is `wide_deep_model` then you can use this command to zip it up:

```
tar -zcvf wide_deep_model.tar.gz wide_deep_model
```

The unzipped directory structure should look like this:

```
wide_deep_model
wide_deep_model/1
wide_deep_model/1/variables
wide_deep_model/1/saved_model.pb
wide_deep_model/1/variables/variables.data-00000-of-00001
wide_deep_model/1/variables/variables.index
```

## Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/heroku/tf-bridge)

### From Source

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

## Example Model & Client

A pre-made publicly available model is provided here:

```
https://s3.amazonaws.com/octo-public/wide_deep_model.tar.gz
```
Some background information about the science behind this model can be found [here](https://www.tensorflow.org/tutorials/wide_and_deep).

Set the provided URL as a config var via the button deploy or set it manually: 

```
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/octo-public/wide_deep_model.tar.gz -a <your_app_name>
```

If you want to test your server with the provided model, a client and test data have been provided in the `wide-deep` directory. To run the client and test your server:

```
git clone git@github.com:heroku/tf-bridge.git
cd tf-bridge/wide-deep
pipenv --three
pipenv install
pipenv run python wide_deep_client.py <your-appname>.herokuapp.com:80
```

If all goes well you should see:

```
--------------------------
--------------------------
Accuracy:  0.8
--------------------------
--------------------------
```

### Server Benchmarks w/ Example Model

See [`SIEGE.md`](/SIEGE.md) for details

## Notes
1. The [Apt buildpack](https://github.com/heroku/heroku-buildpack-apt) loads `tensorflow-model-server` & deps
1. The [Runit buildpack](https://github.com/danp/heroku-buildpack-runit) manages `tensorflow-serving` & `tf-bridge` processes
1. `.profile.d` script loads models from the `TENSORFLOW_MODEL_URL` config var
1. Models must be exported using the `SavedModelBuilder` module, which is outlined [here](https://www.tensorflow.org/serving/serving_basic)

