from flask import Flask
from pulp import*

app=Flask(__name__)

@app.route("/")
def home():
    return f"Welcome"

@app.route("/optimizacion", methods=["GET", "POST"])
def modelo():
    #modelacion con pulp
    ventanas=LpProblem("modelo_de_optimizacion", LpMaximize)
    x1=LpVariable ("Ventanas_madera", 0)
    x2=LpVariable ("Ventanas_madera", 0)

    ventanas+=60*x1 +30*x2 #F.O
    ventanas+=x1<=6 #R1
    ventanas+=x2<=4 #R2
    ventanas+=6*x1+8*x2<=48 #R3
    return f"{x1.varValue}"


if __name__=="__main__":
    app.run(debug=True)