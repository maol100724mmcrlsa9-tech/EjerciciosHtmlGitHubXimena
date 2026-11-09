from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conectar a la base de datos.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bibliotecalesly'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def Inicio():
    return render_template('contraseña.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        # Validación básica de ejemplo
        if usuario == "admin" and password == "1234":
            return render_template('menu.html')
        else:
            flash('Contraseña incorrecta, vuelve a intentarlo')
            return render_template('menu.html')

@app.route('/Menuprincipal')
def Menuprincipal():
    return render_template('menu.html')

@app.route('/Empleados')
def Empleados():
    return render_template('empleados.html')

# Ir a la Pagina de inicio
@app.route('/Libros')
def Libros():
    cur = mysql.connection.cursor()
    cur.execute('Select * from libros')
    data = cur.fetchall()
    # print(data)
    # return 'Bienvenidos al sistema Bibliotecario 1.0'
    return render_template('libros.html', libros=data)

@app.route('/Bienvenidos')
def Bienvenidos():
    return render_template('Bienvenidos.html')

@app.route('/Agregar_Libro', methods=['POST'])
def Agregar_Libro():
    # return 'Modulo: Agregar Libro'
    if request.method == 'POST':
        id = request.form['id']
        titulo = request.form['titulo']
        autor = request.form['autor']
        edicion = request.form['edicion']
        año = request.form['año']
        editorial = request.form['editorial']
        nopaginas = request.form['nopaginas']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO libros (Titulo, Autor, Edicion, Año, Editorial, NoPaginas) ' \
        'VALUES (%s,%s,%s,%s,%s,%s)', \
        (titulo, autor, edicion, año, editorial, nopaginas))
        mysql.connection.commit()
        flash('Libro Agregado satisfactoriamente')
        return redirect(url_for('Libros'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)