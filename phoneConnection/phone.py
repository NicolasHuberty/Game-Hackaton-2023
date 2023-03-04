from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__)

global_var = True
bonus1 = True
bonus2 = True
bonus3 = True
bonus4 = True

pointsPlayer1 = 14
pointsPlayer2 = 19
activeBonus = []
pause = False
bonus5 = True
bonus6 = True
bonus7 = True
bonus8 = True



@app.route('/update_bonus', methods=['POST'])
def update_bonus():
    global bonus1, bonus2, bonus3, bonus4,bonus5, bonus6, bonus7, bonus8
    bonus = str(request.form['bonus'])
    bonusValue = request.form.get('bonusValue')
    if bonus == 'bonus1' : bonus1 = bonusValue
    elif bonus == 'bonus2' : bonus2 = bonusValue
    elif bonus == 'bonus3' : bonus3 = bonusValue
    elif bonus == 'bonus4' : bonus4 = bonusValue
    elif bonus == 'bonus5' : bonus5 = bonusValue
    elif bonus == 'bonus6' : bonus6 = bonusValue
    elif bonus == 'bonus7' : bonus7 = bonusValue
    elif bonus == 'bonus8' : bonus8 = bonusValue
    
    return f"{bonus} : {bonusValue}"

@app.route('/update_pause', methods=['POST'])
def update_pause():
    global pause
    pause = str(request.form['pause'])
     
    
    return f"py pause : {pause}"


@app.route('/recupValeurInPy')
def get_bonus1():
    return jsonify(bonus1,bonus2,bonus3,bonus4,pointsPlayer1,pointsPlayer2,pause,bonus5,bonus6,bonus7,bonus8)



@app.route("/")
def index():
    # Pass global variable value to template
    return render_template("index.html", global_var=global_var)

"""@app.route("/toggle")
def toggle():
    # Toggle global variable value on button click
    global global_var
    global_var = not global_var
    return render_template("index.html", global_var=global_var)
"""

@app.route("/player1")
def player1():
    # Pass global variable value to template
    return render_template("player1.html", global_var=global_var)

@app.route("/player2")
def player2():
    # Pass global variable value to template
    return render_template("player2.html", global_var=global_var)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)