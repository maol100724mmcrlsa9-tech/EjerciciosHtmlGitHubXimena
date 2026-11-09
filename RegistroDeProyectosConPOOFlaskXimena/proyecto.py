class Proyecto:
    def __init__(self, nombre, responsable, descripcion, estado, asignatura, dias_restantes):
        self.nombre = nombre
        self.responsable = responsable
        self.descripcion = descripcion
        self.estado = estado
        self.asignatura = asignatura
        self.dias_restantes = dias_restantes

    def mostrar_informacion(self):
        return f"{self.nombre} - {self.responsable} - {self.estado}"

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado