class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota del alumno: {self.nota}")
    
    def resultado(self):
        if self.nota >= 6:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} ha desaprobado con una nota de {self.nota}.")


alumno1 = Alumno("Victor", 7)


alumno1.imprimir()
alumno1.resultado()
