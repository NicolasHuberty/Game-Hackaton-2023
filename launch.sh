kill -9 $(lsof -t -i:5000)
python3 testReq.py &
python3 game_copy.py
