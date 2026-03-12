from flask import Flask, render_template, request
from pulp import *

app=Flask(__name__)

@app.route("/")
def home():
    return f"Welcome"

@app.route("/optimizacion", methods=["GET", "POST"])
def modelo():

    if request.method=="POST":
        madera=float(request.form.get("madera"))
        aluminio=float(request.form.get("aluminio"))

        #modelacion con pulp
        ventanas=LpProblem("modelo_de_optimizacion", LpMaximize)
        x1=LpVariable ("Ventanas_madera", 0)
        x2=LpVariable ("Ventanas_aluminio", 0)

        ventanas+= madera*x1+aluminio*x2 #F.O
        ventanas+=x1<=6 #R1
        ventanas+=x2<=4 #R2
        ventanas+=6*x1+8*x2<=48 #R3

        ventanas.solve()
        
        res1=x1.varValue
        res2=x2.varValue
        fo=value(ventanas.objective)

        return render_template("Optimizacion.html", res1=res1, res2=res2, fo=fo)
    return render_template("Optimizacion.html")


if __name__=="__main__":
    app.run(debug=True)