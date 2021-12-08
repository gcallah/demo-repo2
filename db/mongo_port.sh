#!/bin/bash

export passwd=$MONGO_PASSWD
export db="chatDB"
export collect="rooms"
export key="roomName"

python3 mongo_port.py $db $collect $key $passwd
