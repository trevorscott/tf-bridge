
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
*********** Done Exporting at PAth - /tmp/census_exported/1524171786
```

Then move it and zip it up and save it to s3:

```
mv /tmp/census_exported/1524171786/ /Users/tscott/heroku/tensorflow/models/wide-deep2/1
cd /Users/tscott/heroku/tensorflow/models/
tar -zcvf wide_deep2_model.tar.gz wide-deep2
```

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