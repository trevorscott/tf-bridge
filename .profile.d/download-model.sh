#Download model from user provided URL
mkdir -p /app/.tf-model
cd /app/.tf-model
curl $TENSORFLOW_MODEL_URL --output $TENSORFLOW_MODEL_NAME.tar.gz
tar -zxvf $TENSORFLOW_MODEL_NAME.tar.gz
cd /app

