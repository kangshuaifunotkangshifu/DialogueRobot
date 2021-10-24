#!/bin/bash
source /usr/local/anaconda3/etc/profile.d/conda.sh
conda activate robot
git -C ~/DialogueRobot pull
python ~/DialogueRobot/DiaRobot/manage.py runserver 0.0.0.0:8080
