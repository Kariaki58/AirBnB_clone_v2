#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
if test -d "/etc/nginx"; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static {/,$d' "$nginx_config"
sudo sed -i '/server_name _;/ a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' "$nginx_config"

sudo service nginx restart
