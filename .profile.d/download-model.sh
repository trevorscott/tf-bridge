#Download model from user provided URL
mkdir -p /app/.tf-model
cd /app/.tf-model
curl $TENSORFLOW_MODEL_URL --output default.tar.gz
tar -zxvf default.tar.gz

OLD_DIR_NAME="$(ls -I default.tar.gz)"
mv $OLD_DIR_NAME default

cd /app

