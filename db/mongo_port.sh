#!/bin/bash

export passwd=$MONGO_PASSWD
export db="chatDB"
export collect="users"
export key="userName"

python3 mongo_port.py $db $collect $key $passwd
