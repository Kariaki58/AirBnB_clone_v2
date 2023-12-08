#!/usr/bin/env bash
# prepare your web servers

if [ ! -d "/etc/nginx/" ]; then
	sudo apt-get -y upgrade
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

mkdir -p /data /data/web_static /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee data/web_static/releases/test/index.html
sudo ln -sfT /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
nginx_conf="/etc/nginx/sites-available/default"
nginx_alias_config="location /hbnb_static/ { alias /data/web_static/current/; }"
if ! sudo grep -qF "$nginx_alias_config" "$nginx_config"; then
	    sudo sed -i "/server {/a $nginx_alias_config" "$nginx_config"
fi
sudo service nginx restart
