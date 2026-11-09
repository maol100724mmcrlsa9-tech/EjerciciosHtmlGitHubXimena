from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola a todos bienvenidos al curso de aplicaciones web con Python, haciendo uso de Aplicaciones Web...'

if __name__ == '__main__':
    app.run(debug=True)