#!/usr/bin/env bash
# Creating a custom HTTP header response, but with Puppet.

sudo apt-get update
sudo apt-get install -y nginx

echo "Hello World!" | sudo tee /var/www/html/index.html

redirection="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=Htqn7tGvQsc permanent;"
sudo sed -i "s/server_name _;/$redirection/" /etc/nginx/sites-enabled/default


echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
error="listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}"
sudo sed -i "s/listen 80 default_server;/$error/" /etc/nginx/sites-enabled/default

sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default

sudo nginx -t
sudo service nginx restart
