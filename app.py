from flask import Flask , render_template


#acc = 0.0
#rec = 0.0
#prec = 0.0
#f1 = 0.0
#r2 = 0.0

#import cancer_detection as mlp_cancer


app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route('/metricas')

def metricas():
  
  return render_template("metricas.html") 

@app.route('/info')

def info():
    return render_template("info.html")

@app.route('/graficas')

def grafica():
    return render_template("graficas.html")

if __name__ == "__main__":
    app.run(debug=True)
