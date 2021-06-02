#!/bin/bash
echo " "
echo " "

echo "<<<<<<<<<<< Installing requirements >>>>>>>>>>>>>>"
echo " "
$(cat .env.dev | xargs)
export $(cat .env | xargs)
make install

echo ‘'<<<<<<<<<<<<<<' Run migration '>>>>>>>>>>>>>>>>>>>>>>>'’

echo " "

make migrate

echo "<<<<<<<<<<<<<< Drop stale data >>>>>>>>>>>>>>>>>>>>"

make hard_delete

echo "<<<<<<<<<<<<<< Daemon reload >>>>>>>>>>>>>>>>>>>>"
sudo systemctl daemon-reload

echo "<<<<<<<<<<<<<< Restarting gunicorn >>>>>>>>>>>>>>>>>>>>"
sudo  systemctl restart gunicorn

echo " "
echo " "
echo "<<<<<<<<<<<<<<<< Restarting nginx >>>>>>>>>>>>>>>>>>>>>>"
echo " "

sudo systemctl restart nginx

exit
