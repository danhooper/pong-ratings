#!/bin/bash

sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get -y install git python-pip sqlite3 nginx supervisor
sudo pip install virtualenv
mkdir -p ~/git
cd ~/git
if [ -d ~/git/pong-ratings ] ; then
    cd ~/git/pong-ratings
    git pull
else
    git clone https://github.com/danhooper/pong-ratings.git
fi
mkdir -p ~/virtualenv
cd ~/virtualenv
virtualenv ~/virtualenv/pong_ratings
source ~/virtualenv/pong_ratings/bin/activate
pip install --upgrade setuptools
pip install -r ~/git/pong-ratings/src/pong_ratings/requirements/project.txt
cd ~/git/pong-ratings/src/pong_ratings
python manage.py syncdb --noinput
cd ~/git/pong-ratings/local
sudo cp nginx/pong_ratings.conf /etc/nginx/conf.d/
sudo cp supervisor/pong_ratings.conf /etc/supervisor/conf.d/
sudo rm /etc/nginx/sites-enabled/default
sudo service supervisor start
sudo supervisorctl reread
sudo supervisorctl update
sudo service nginx start
