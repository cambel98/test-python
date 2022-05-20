class Persona:
  def __init__(self, _nombre, _edad, _nacionalidad):
    self.nombre = _nombre
    self.edad = _edad
    self.nacionalidad = _nacionalidad

  def cumpleanios(self):
    self.edad += 1

  def __str__(self):
    return "Persona: " + self.nombre + " que tiene " + self.edad + " años y es de nacionalidad " + self.nacionalidad


p = Persona("Oscar", 23, "peruana")
print(p)

