class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_edad(self, edad):
        self.edad = edad
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def print_persona(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18


persona1 = Persona("Victor", 25)
persona2 = Persona("Ana", 17)


print(f"{persona1.get_nombre()} es mayor de edad: {persona1.es_mayor_de_edad()}")
print(f"{persona2.get_nombre()} es mayor de edad: {persona2.es_mayor_de_edad()}")
