from flask import Flask , render_template




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
