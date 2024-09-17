from abc import ABC, abstractmethod

class SerVivo(ABC):
  def __init__(self, idade, habitat, alimentacao):
    self._idade = idade
    self._habitat = habitat
    self._alimentacao = alimentacao
  
  def __str__(self):
    return f'de {self.idade} ano(s), vive em {self.habitat}s e se alimenta de {self.alimentacao}'
  
  @property
  def idade(self):
    return self._idade
  
  @property
  def habitat(self):  
    return self._habitat
  
  @property
  def alimentacao(self):  
    return self._alimentacao
  
  @abstractmethod
  def alimentar_se(self):
    pass