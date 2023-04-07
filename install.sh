echo '--- Install selenium driver'
./install_selenium.sh
echo '--- Install dependencies'
sudo apt install python3-pip
pip3 install --upgrade pip
pip3 install -r requirements.txt
python -V
echo '--- Create file for phones'
touch phones.txt