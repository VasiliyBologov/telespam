echo '--- Download selenium driver'

mkdir selenium
#cd /selenium/

# https://chromedriver.chromium.org/downloads

wget https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip -O ./selenium/chromedriver.zip

sudo apt-get install unzip

unzip ./selenium/chromedriver.zip -d ./selenium/