#clase
class Perros:
    def __init__(self, nombre, raza, edad, peso, sexo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.sexo = sexo
        
p1 = Perros("Tami", "Bulldog", 11, 20, "masculino")
print(p1.nombre)
