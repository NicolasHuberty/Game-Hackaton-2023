#!/bin/bash

# Launch first command in new tab
gnome-terminal --tab --title="Flask" --command="python3 testReq.py"

# Launch second command in new tab
gnome-terminal --tab --title="Tab 2" --command=" sleep 5 | python3 game_copy.py"
