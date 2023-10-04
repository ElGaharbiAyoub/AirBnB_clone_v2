#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e "<html>
<head>
  </head>
  <body>
    <h1>welcome</h1>
    <h3>I'm ayoub el gharbi from ALX Africa</h3>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
file=/etc/nginx/sites-available/default
phrase="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n}\n"
sudo sed -i "42i $phrase" $file
sudo service nginx restart
