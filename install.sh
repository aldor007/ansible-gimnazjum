#!/bin/bash
apt-get install python-apt -y 
apt-get install sudo -y 
apt-get install python-dev -y 
apt-get install python-pip -y
apt-get install sshpass -y
apt-get install python-pip
apt-get install python-yaml

apt-get install libcgi-pm-perl
apt-get install rrdtool
apt-get install librrds-perl
cpan JSON

mkdir -p /var/www/collect/
cd /var/www; wget https://github.com/downloads/httpdss/collectd-web/collectd-web_0.4.0.tar.gz; tar -zxvf collectd-web_0.4.0.tar.gz

pip install ansible
pip install passlib

