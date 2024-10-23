class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def sumar(self):
        return self.valor1 + self.valor2
    
    def restar(self):
        return self.valor1 - self.valor2
    
    def multiplicar(self):
        return self.valor1 * self.valor2
    
    def dividir(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "No se puede dividir por cero."


valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))


calculadora = Calculadora(valor1, valor2)


print(f"Suma: {calculadora.sumar()}")
print(f"Resta: {calculadora.restar()}")
print(f"Multiplicación: {calculadora.multiplicar()}")
print(f"División: {calculadora.dividir()}")
