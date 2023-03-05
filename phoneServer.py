from flask import Flask, render_template, request, jsonify
import os
app = Flask(__name__)

global_var = True

class sizeBluePadle():
    def __init__(self):
        self.sizeBluePadle  = 140
    def get(self):
        return self.sizeBluePadle 
    def set(self,value):
        self.sizeBluePadle  = value
sizeBluePadle = sizeBluePadle()

class sizeRedPadle():
    def __init__(self):
        self.sizeRedPadle  = 140
    def get(self):
        return self.sizeRedPadle 
    def set(self,value):
        self.sizeRedPadle  = value
sizeRedPadle = sizeRedPadle()
class x1():
    def __init__(self):
        self.x1 = 0
    def get(self):
        return self.x1
    def set(self,value):
        self.x1 = value
x1 = x1()
class x2():
    def __init__(self):
        self.x2 = 0
    def get(self):
        return self.x2
    def set(self,value):
        self.x2 = value
x2 = x2()
class bonus1():
    def __init__(self):
        self.bonus1 = True
    def get(self):
        return self.bonus1
    def set(self,value):
        self.bonus1 = value
bonus1 = bonus1()

class bonus2():
    def __init__(self):
        self.bonus2 = True
    def get(self):
        return self.bonus2
    def set(self,value):
        self.bonus2 = value
bonus2 = bonus2()

class bonus3():
    def __init__(self):
        self.bonus3 = True
    def get(self):
        return self.bonus3
    def set(self,value):
        self.bonus3 = value
bonus3 = bonus3()

class bonus4():
    def __init__(self):
        self.bonus4 = True
    def get(self):
        return self.bonus4
    def set(self,value):
        self.bonus4 = value
bonus4 = bonus4()

class bonus5():
    def __init__(self):
        self.bonus5 = True
    def get(self):
        return self.bonus5
    def set(self,value):
        self.bonus5 = value
bonus5 = bonus5()

class bonus6():
    def __init__(self):
        self.bonus6 = True
    def get(self):
        return self.bonus6
    def set(self,value):
        self.bonus6 = value
bonus6 = bonus6()

class bonus7():
    def __init__(self):
        self.bonus7 = True
    def get(self):
        return self.bonus7
    def set(self,value):
        self.bonus7 = value
bonus7 = bonus7()

class bonus8():
    def __init__(self):
        self.bonus8 = True
    def get(self):
        return self.bonus8
    def set(self,value):
        self.bonus8 = value
bonus8 = bonus8()

class pointsPlayer1 ():
    def __init__(self):
        self.pointsPlayer1  = 0
    def get(self):
        return self.pointsPlayer1 
    def set(self,value):
        self.pointsPlayer1  = value
        
pointsPlayer1 = pointsPlayer1()

class pointsPlayer2 ():
    def __init__(self):
        self.pointsPlayer2  = 0
    def get(self):
        return self.pointsPlayer2 
    def set(self,value):
        self.pointsPlayer2  = value
pointsPlayer2 = pointsPlayer2()


class start ():
    def __init__(self):
        self.start  = -1
    def get(self):
        return self.start
    def set(self,value):
        self.start  = value
start = start()

class pause ():
    def __init__(self):
        self.pause  = False
    def get(self):
        return self.pause 
    def set(self,value):
        self.pause  = value
pause = pause()




@app.route('/update_bonus', methods=['POST'])
def update_bonus():
    bonus = str(request.form['bonus'])
    bonusValue = request.form.get('bonusValue')
    if bonus == 'bonus1' : bonus1.set(bonusValue)
    elif bonus == 'bonus2' : bonus2.set(bonusValue)
    elif bonus == 'bonus3' : bonus3.set(bonusValue)
    elif bonus == 'bonus5' : bonus5.set(bonusValue)
    elif bonus == 'bonus6' : bonus6.set(bonusValue)
    elif bonus == 'bonus7' : bonus7.set(bonusValue)
    elif bonus == 'bonus8' : bonus8.set(bonusValue)
    return f"{bonus} : {bonusValue}"

@app.route('/start', methods=['POST'])
def start_game():
     mapNumber = int(request.form['mapNumber'])
     start.set(mapNumber)
     return f"Le jeux à commencé sur la map : {mapNumber}"
     
        
@app.route('/update_pause', methods=['POST'])
def update_pause():
    print()
    print("PAUSE VAL:",(str(request.form['pause']) == "true"))
    pause.set(str(request.form['pause']) == "true")
    return f"py pause : {pause}"

@app.route('/updatePoints',methods=['POST'])
def updatePoints():
    pointsPlayer1.set(int(request.form.get("pointsPlayer1")))
    pointsPlayer2.set(int(request.form.get("pointsPlayer2")))
    return f"py pause : {pointsPlayer1.get(),pointsPlayer2.get()}"

@app.route('/recupValeurInPy')
def get_bonus1():
    return jsonify(bonus1.get(),bonus2.get(),bonus3.get(),bonus4.get(),pointsPlayer1.get(),pointsPlayer2.get(),pause.get(),bonus5.get(),bonus6.get(),bonus7.get(),bonus8.get(),start.get())





@app.route("/")
def index():
    """
    IMGFOLDER= os.path.join("static",'templates')
    app.config[]"""
    #filename = os.path.join(app.config["./"],"map0.png")
    # Pass global variable value to template
    return render_template("index.html", global_var=global_var)


@app.route("/player1")
def player1():
    # Pass global variable value to template
    return render_template("player1.html", global_var=global_var)
global_var
@app.route("/player2")
def player2():
    # Pass global variable value to template
    return render_template("player2.html", global_var=global_var)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False,use_reloader=False)