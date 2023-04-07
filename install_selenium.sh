echo '--- Download selenium driver'

mkdir selenium
#cd /selenium/

# https://chromedriver.chromium.org/downloads

wget https://chromedriver.storage.googleapis.com/111.0.5563.64/chromedriver_linux64.zip -O ./selenium/chromedriver.zip

apt-get install unzip

unzip ./selenium/chromedriver.zip -d ./selenium/