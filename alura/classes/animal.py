from ser_vivo import SerVivo

class Animal(SerVivo):
  def __init__(self, idade, habitat, alimentacao, raca, genero):
    super().__init__(idade, habitat, alimentacao)
    self._raca = raca
    self._genero = genero

  def __str__(self):
    return f'O {self.raca} {self.genero}' + super().__str__()
  
  @property
  def raca(self):
    return self._raca
  
  @property
  def genero(self):
    return self._genero
  
  def alimentar_se(self):
    pass