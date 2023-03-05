#!/bin/bash

# Launch first command in new tab
gnome-terminal --tab --title="Flask"  -- bash -c "python3 phoneServer.py"

# Launch second command in new tab
gnome-terminal --tab --title="Game"  -- bash -c "python3 game.py"
