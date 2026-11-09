from flask import Flask, render_template, request, redirect, url_for, flash
from proyecto import Proyecto
from base_datos import (
    crear_tabla,
    insertar_proyecto,
    obtener_proyectos,
    obtener_proyecto,
    actualizar_estado,
    eliminar_proyecto,
)

app = Flask(__name__)
app.secret_key = "clave_temporal_dia5"

crear_tabla()

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        responsable = request.form["responsable"].strip()
        descripcion = request.form["descripcion"].strip()
        estado = request.form["estado"].strip()
        asignatura = request.form["asignatura"].strip()
        dias_restantes = request.form["dias_restantes"].strip()
        if not nombre or not responsable or not descripcion or not estado or not asignatura or not dias_restantes:
            flash("Completa todos los campos.")
            return redirect(url_for("registrar"))
        nuevo_proyecto = Proyecto(
            nombre,
            responsable,
            descripcion,
            estado,
            asignatura,
            int(dias_restantes),
        )
        insertar_proyecto(nuevo_proyecto)
        flash("Proyecto registrado correctamente.")
        return redirect(url_for("ver_proyectos"))
    return render_template("registrar.html")

@app.route("/proyectos")
def ver_proyectos():
    proyectos = obtener_proyectos()
    return render_template("proyectos.html", proyectos=proyectos)

@app.route("/editar/<int:id_proyecto>", methods=["GET", "POST"])
def editar_proyecto(id_proyecto):
    proyecto = obtener_proyecto(id_proyecto)
    if request.method == "POST":
        actualizar_estado(id_proyecto, request.form["estado"])
        flash("Estado del proyecto actualizado correctamente.")
        return redirect(url_for("ver_proyectos"))
    return render_template("editar.html", proyecto=proyecto)

@app.route("/eliminar/<int:id_proyecto>", methods=["POST"])
def borrar_proyecto(id_proyecto):
    eliminar_proyecto(id_proyecto)
    flash("Proyecto eliminado correctamente.")
    return redirect(url_for("ver_proyectos"))

if __name__ == "__main__":
    app.run()