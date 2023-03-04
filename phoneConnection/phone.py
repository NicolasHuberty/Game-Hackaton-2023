from flask import Flask, render_template, request
 
app = Flask(__name__)

# Define global variable
global_var = False

@app.route("/")
def index():
    # Pass global variable value to template
    return render_template("index.html", global_var=global_var)

@app.route("/toggle")
def toggle():
    # Toggle global variable value on button click
    global global_var
    global_var = not global_var
    return render_template("index.html", global_var=global_var)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
