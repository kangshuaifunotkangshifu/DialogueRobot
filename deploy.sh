#!/bin/bash
conda activate robot
git -C ~/DialogueRobot pull
python ~/DialogueRobot/DiaRobot/manage.py runserver 0.0.0.0:8080
