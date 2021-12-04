#!/bin/bash

export passwd="1D9u0b4l%21"
export db="chatDB"
export collect="rooms"
export key="name"

python3 mongo_port.py $db $collect $key $passwd
