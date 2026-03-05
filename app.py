from flask import Flask, render_template
from pulp import *

app=Flask(__name__)

@app.route("/")
def home():
    return f"Welcome"

@app.route("/optimizacion", methods=["GET", "POST"])
def modelo():
    #modelacion con pulp
    ventanas=LpProblem("modelo_de_optimizacion", LpMaximize)
    x1=LpVariable ("Ventanas_madera", 0)
    x2=LpVariable ("Ventanas_aluminio", 0)

    ventanas+=60*x1 +30*x2 #F.O
    ventanas+=x1<=6 #R1
    ventanas+=x2<=4 #R2
    ventanas+=6*x1+8*x2<=48 #R3

    ventanas.solve()
    
    res1=x1.varValue
    res2=x2.varValue

    return render_template("Optimizacion.html", res1=res1, res2=res2)

if __name__=="__main__":
    app.run(debug=True)