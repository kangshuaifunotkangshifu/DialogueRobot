#!/bin/bash
tmux kill-session -t django
tmux new-session -d -s django
tmux send-keys "cd ~/DialogueRobot" C-m
tmux send-keys "git pull" C-m
tmux send-keys "cd ~/DialogueRobot/DiaRobot" C-m
tmux send-keys "conda activate robot" C-m
tmux send-keys "python manage.py runserver 0.0.0.0:8080" C-m
