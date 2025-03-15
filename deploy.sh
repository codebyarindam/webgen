#!/bin/bash
cd /home/myblock/Documents/Arindam/codegen
npm run build
sudo cp -r build/* /var/www/html/codegen-app/
sudo chown -R www-data:www-data /var/www/html/codegen-app
sudo chmod -R 755 /var/www/html/codegen-app
echo "Deployment successful!"
