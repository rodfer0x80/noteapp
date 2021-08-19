#!/bin/sh

docker ps

echo ""
read -p "Container ID: " CONTAINER_ID

docker exec -it $CONTAINER_ID psql -U noteapp noteapp_notes


#sudo -u postgres -i
