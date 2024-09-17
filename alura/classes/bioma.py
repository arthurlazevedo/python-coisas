from typing import List
from ser_vivo import SerVivo
from planta import Planta
from animal import Animal

class Bioma:
  def __init__(self, nome, tipo, clima):
    self._nome = nome
    self._tipo = tipo
    self._clima = clima
    self._seres_vivos: List[SerVivo] = []

  def __str__(self):
    return f'{self.nome} é um bioma {self.tipo} com clima {self.clima}. As principais espécies que vivem lá são: {self.seres_vivos}'
  
  @property
  def nome(self):
    return self._nome
  
  @property
  def tipo(self):  
    return self._tipo
  
  @property
  def clima(self):  
    return self._clima
  
  @property
  def seres_vivos(self):
    lista_seres = []
    for ser_vivo in self._seres_vivos:
      if isinstance(ser_vivo, Animal):      
        lista_seres.append(ser_vivo.raca)
      elif isinstance(ser_vivo, Planta):
        lista_seres.append(ser_vivo.familia)
    return ', '.join(lista_seres)
  
  def adicionar_especie(self, ser_vivo):
    if isinstance(ser_vivo, SerVivo):
      self._seres_vivos.append(ser_vivo)

  @property
  def listar_seres_vivos(self):
    for i,item in enumerate(self._seres_vivos, 1):
      if hasattr(item, 'raca'):
        print(f'{i}. (Animal):' + item.__str__())
      else:
        print(f'{i}. (Planta):' + item.__str__())
    
    # provavelmente é possível pegar o nome da classe para simplificar isso, mas queria deixar o hasattr para eu não esquecer