from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_biblioteca_secret'
NOMBRE_DB = 'proyectos.db'

def obtener_conexion():
    conexion = sqlite3.connect(NOMBRE_DB)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tablas():
    conexion = obtener_conexion()
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT NOT NULL,
            curp TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

crear_tablas()

# Ruta Principal y Login
@app.route('/')
@app.route('/Login')
def inicio():
    return render_template('menu.html')

# Ruta de Libros (evita el error 404 si entras a /Libros)
@app.route('/Libros')
def Libros():
    return render_template('libros.html')

# Rutas de Usuarios
@app.route('/Usuarios')
def Usuarios():
    conexion = obtener_conexion()
    usuarios = conexion.execute('SELECT * FROM usuarios').fetchall()
    conexion.close()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/Agregar_Usuario', methods=['POST'])
def Agregar_Usuario():
    if request.method == 'POST':
        id_user = request.form['id'].strip()
        nombre = request.form['nombre'].strip()
        direccion = request.form['direccion'].strip()
        telefono = request.form['telefono'].strip()
        correo = request.form['correo'].strip()
        curp = request.form['curp'].strip()

        conexion = obtener_conexion()
        conexion.execute(
            'INSERT INTO usuarios (id, nombre, direccion, telefono, correo, curp) VALUES (?, ?, ?, ?, ?, ?)',
            (id_user, nombre, direccion, telefono, correo, curp)
        )
        conexion.commit()
        conexion.close()
        flash('Usuario Agregado satisfactoriamente')
        return redirect(url_for('Usuarios'))

@app.route('/ModificarUsuario/<int:id>')
def ModificarUsuario(id):
    conexion = obtener_conexion()
    usuario = conexion.execute('SELECT * FROM usuarios WHERE id = ?', (id,)).fetchone()
    conexion.close()
    return render_template('modificarUsuarios.html', usuarios=usuario)

@app.route('/ActualizarUsuario/<int:id>', methods=['POST'])
def ActualizarUsuario(id):
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        direccion = request.form['direccion'].strip()
        telefono = request.form['telefono'].strip()
        correo = request.form['correo'].strip()
        curp = request.form['curp'].strip()

        conexion = obtener_conexion()
        conexion.execute("""
            UPDATE usuarios
            SET nombre = ?, direccion = ?, telefono = ?, correo = ?, curp = ?
            WHERE id = ?
        """, (nombre, direccion, telefono, correo, curp, id))
        conexion.commit()
        conexion.close()
        flash('Usuario actualizado exitosamente')
        return redirect(url_for('Usuarios'))

@app.route('/EliminarUsuario/<int:id>', methods=['POST', 'GET'])
def EliminarUsuario(id):
    conexion = obtener_conexion()
    conexion.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
    flash('Usuario eliminado satisfactoriamente')
    return redirect(url_for('Usuarios'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)