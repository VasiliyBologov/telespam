echo '--- Install selenium driver'
./install_selenium.sh
echo '--- Install dependencies'
pip install --upgrade pip
pip install -r requirements.txt
python -V
echo '--- Create file for phones'
touch phones.txt