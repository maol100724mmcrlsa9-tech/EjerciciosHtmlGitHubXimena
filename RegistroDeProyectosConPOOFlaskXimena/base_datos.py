import sqlite3

NOMBRE_BASE_DATOS = "proyectos.db"

def conectar():
    conexion = sqlite3.connect(NOMBRE_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla():
    conexion = conectar()
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS proyectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            responsable TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            estado TEXT NOT NULL,
            asignatura TEXT NOT NULL,
            dias_restantes INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def insertar_proyecto(proyecto):
    conexion = conectar()
    conexion.execute("""
        INSERT INTO proyectos 
        (nombre, responsable, descripcion, estado, asignatura, dias_restantes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        proyecto.nombre,
        proyecto.responsable,
        proyecto.descripcion,
        proyecto.estado,
        proyecto.asignatura,
        proyecto.dias_restantes
    ))
    conexion.commit()
    conexion.close()

def obtener_proyectos():
    conexion = conectar()
    proyectos = conexion.execute(
        "SELECT * FROM proyectos ORDER BY id DESC"
    ).fetchall()
    conexion.close()
    return proyectos

def obtener_proyecto(id_proyecto):
    conexion = conectar()
    proyecto = conexion.execute(
        "SELECT * FROM proyectos WHERE id = ?", (id_proyecto,)
    ).fetchone()
    conexion.close()
    return proyecto

def actualizar_estado(id_proyecto, nuevo_estado):
    conexion = conectar()
    conexion.execute(
        "UPDATE proyectos SET estado = ? WHERE id = ?",
        (nuevo_estado, id_proyecto),
    )
    conexion.commit()
    conexion.close()

def eliminar_proyecto(id_proyecto):
    conexion = conectar()
    conexion.execute(
        "DELETE FROM proyectos WHERE id = ?", (id_proyecto,)
    )
    conexion.commit()
    conexion.close()