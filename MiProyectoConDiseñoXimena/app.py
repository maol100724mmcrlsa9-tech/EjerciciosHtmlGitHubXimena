from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal que muestra el menú de paisajes
@app.route("/")
def Inicio():
    return render_template("inicio.html")

# Rutas para cada paisaje
@app.route('/Paisaje1')
def Paisaje1():
    return render_template('archivo1.html')

@app.route('/Paisaje2')
def Paisaje2():
    return render_template('archivo2.html')

@app.route('/Paisaje3')
def Paisaje3():
    return render_template('archivo3.html')

if __name__ == '__main__':
    app.run(debug=True)