#!/bin/bash
port=8080
pid=$(netstat -nlp | grep :$port | awk '{print $7}' | awk -F"/" '{print $1}')
if [ -n "$pid" ]; then
    kill -9 $pid;
fi

source /usr/local/anaconda3/etc/profile.d/conda.sh
conda activate robot
git -C ~/DialogueRobot pull
python ~/DialogueRobot/DiaRobot/manage.py runserver 0.0.0.0:8080
