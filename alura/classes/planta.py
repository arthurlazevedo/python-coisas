from ser_vivo import SerVivo

class Planta(SerVivo):
  def __init__(self, idade, habitat, alimentacao, tipo, familia):
    super().__init__(idade, habitat, alimentacao)
    self._tipo = tipo
    self._familia = familia

  def __str__(self):
    return f'A {self.familia} é uma planta {self.tipo}' + super().__str__()
  
  @property
  def tipo(self):
    return self._tipo
  
  @property
  def familia(self):
    return self._familia
  
  def alimentar_se(self):
    pass