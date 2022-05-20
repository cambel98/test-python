class Persona:
  def __init__(self, _nombre, _edad, _nacionalidad, _saldo):
    self.nombre = _nombre
    self.edad = _edad
    self.saldo = _saldo
    self.nacionalidad = _nacionalidad

  def cumpleanios(self):
    self.edad += 1

  def transferencia(self, persona2, monto):
    if self.saldo >= monto:
      self.saldo -= monto
      persona2.saldo += monto
      print("Transferencia hecha!")
    else:
      print("Saldo insuficiente!")

  def __str__(self):
    return "Persona: " + self.nombre


p = Persona("Jose", 10, "peruana", 2)
p2 = Persona("Pedro", 20, "peruana", 20)
p2.transferencia(p, 7)

print("Saldo de p2: ")
print(p2.saldo)
print("Saldo de p1: ")
print(p.saldo)
