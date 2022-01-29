from flask import Flask , render_template , request , url_for


acc = 0.0
rec = 0.0
prec = 0.0
f1 = 0.0
r2 = 0.0

import cancer_detection as mlp_cancer


app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route('/metricas' , methods =["GET","POST"])

def metricas():
    if request.method == "POST":
         neuronas = request.form["neuronas"]
         epocas = request.form["epocas"]
         optimizador = request.form["optimizador"]
         acc , rec , prec , f1 , r2 = mlp_cancer.predict_cancer(neuronas,epocas,optimizador)
         print(acc)
         print(rec)
         print(prec)
         print(f1)
         print(r2)
         exac = acc
         recall = rec
    return render_template("metricas.html" , accuracy = exac , sensi = recall , precision = prec , f1score = f1,
    coefr2 = r2) 
@app.route('/info')

def info():
    return render_template("info.html")

@app.route('/graficas')

def grafica():
    return render_template("graficas.html")

if __name__ == "__main__":
    app.run(debug=True)
