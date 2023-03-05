from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__)

global_var = True
bonus1 = True
bonus2 = True
bonus3 = True
bonus4 = True
pointsPlayer1 = 0
pointsPlayer2 = 0
activeBonus = []
pause = False
bonus5 = True
bonus6 = True
bonus7 = True
bonus8 = True



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

@app.route('/update_pause', methods=['POST'])
def update_pause():
    pause.set(str(request.form['pause']))
    return f"py pause : {pause}"

@app.route('/updatePoints',methods=['POST'])
def updatePoints():
    print("Receive update")
    pointsPlayer1 = request.form.get("pointsPlayer1")
    pointsPlayer2 = request.form.get("pointsPlayer2")
    pointsPlayer1.set(pointsPlayer1)
    pointsPlayer2.set(pointsPlayer2)
    print("NOWWW:",pointsPlayer1)
    print("OK:",pointsPlayer2)
@app.route('/recupValeurInPy')
def get_bonus1():
    return jsonify(bonus1,bonus2,bonus3,bonus4,pointsPlayer1,pointsPlayer2,pause,bonus5,bonus6,bonus7,bonus8)



@app.route("/")
def index():
    # Pass global variable value to template
    return render_template("index.html", global_var=global_var)


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