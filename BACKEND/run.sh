#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=server
export FLASK_ENV=developer
flask run --host=0.0.0.0 --port=80
