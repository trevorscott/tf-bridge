# Tensor Bridge on Heroku

Deploy [tensor-bridge](https://github.com/Babylonpartners/tf-bridge) and [tensorflow-serving](https://www.tensorflow.org/serving/) on a single dyno.

`tensor-bridge` translates REST requests into gRPC and forwards them to `tensorflow-serving`

## Notes
1. The [Apt buildpack](https://github.com/heroku/heroku-buildpack-apt) loads `tensorflow-model-server` & deps
1. The [Runit buildpack](https://github.com/danp/heroku-buildpack-runit) manages `tensorflow-serving` & `tf-bridge` processes
1. .profile.d script loads model at dyno start up
1. Models must be exported using the SavedModelBuilder module, which is outlined [here](https://www.tensorflow.org/serving/serving_basic)


## Deploy

```
heroku create tf-bridge
heroku config:set TENSORFLOW_MODEL_URL=https://s3.amazonaws.com/octo-public/mnist_model.tar.gz
heroku config:set TENSORFLOW_MODEL_NAME=mnist_model
heroku config:set MODEL=/app/.tf-model/mnist_model
heroku buildpacks:add -i 1 https://github.com/heroku/heroku-buildpack-apt.git
heroku buildpacks:add -i 2 https://github.com/heroku/heroku-buildpack-python.git
heroku buildpacks:add -i 3 https://github.com/danp/heroku-buildpack-runit.git
git push heroku heroku-deploy:master
```

## Test the Server

Once the server is up you can test it with `mnist_client.py`.

```
pipenv --three
pipenv install -r requirements.txt
pipenv run python mnist_client.py <your-appname>.herokuapp.com:80
```

If everything went well, you will shortly get the following output

`Inference error rate: 10.4%`




