#!/bin/bash

HOST=127.0.0.1
PORT=8000
if [ $ANUBIS ]
then
    HOST=0.0.0.0
fi

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=API.endpoints flask run --host=$HOST --port=$PORT
