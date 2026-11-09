from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la Conexión a la Base de Datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Si tienes contraseña en MySQL, colócala aquí
app.config['MYSQL_DB'] = 'bibliotecaprofebeto'

mysql = MySQL(app)

# Clave secreta para manejo de sesiones y mensajes flash
app.secret_key = 'mysecretkey'

# Ruta de Login (Inicio)
@app.route("/")
def inicio():
    return render_template("contraseña.html")

# Validación del Formulario de Login
@app.route('/Login', methods=['POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        # Validación de usuario y contraseña de ejemplo
        if usuario == 'admin' and password == '1234':
            return render_template("menu.html")
        else:
            flash('Contraseña incorrecta, vuelve a intentarlo')
            return render_template("contraseña.html")

# Ruta del Menú Principal
@app.route("/Menuprincipal")
def Menuprincipal():
    return render_template("menu.html")

# Ruta de Empleados
@app.route("/Empleados")
def Empleados():
    return render_template("empleados.html")

# Ruta para Consultar Libros
@app.route('/Libros')
def Libros():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libros')
    data = cur.fetchall()
    return render_template('libros.html', libros=data)

# Ruta para Agregar un Nuevo Libro
@app.route('/Agregar_Libro', methods=['POST'])
def Agregar_Libro():
    if request.method == 'POST':
        id = request.form['id']
        titulo = request.form['titulo']
        autor = request.form['autor']
        edicion = request.form['edicion']
        año = request.form['año']
        editorial = request.form['editorial']
        nopaginas = request.form['nopaginas']
        
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO libros (Titulo, Autor, Edicion, Año, Editorial, NoPaginas) VALUES (%s, %s, %s, %s, %s, %s)',
            (titulo, autor, edicion, año, editorial, nopaginas)
        )
        mysql.connection.commit()
        flash('Libro Agregado satisfactoriamente')
        return redirect(url_for('Libros'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)