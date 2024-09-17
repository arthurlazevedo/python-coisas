class Musica:
  musicas = {}

  def __init__(self, nome: str, ano: int, artista: str, segundos: int):
    self._nome = nome
    self._ano = ano
    self._artista = artista
    self._segundos = segundos
    self._historica = False
    Musica.musicas[self] = self.__str__()

  def __str__(self):
    texto_extra = 'É uma música histórica!' if self.historica else ''
    return f'{self.nome} é uma música de {self.artista} lançada em {self.ano}, com duração de {self.duracao} minutos. {texto_extra}'
  
  @property
  def nome(self):
    return self._nome

  @property
  def ano(self):
    return self._ano
  
  @property
  def artista(self):
    return self._artista
  
  @property
  def historica(self):
    return self._historica

  @property
  def duracao(self):
    segundos = self.segundos % 60 if len(int(self.segundos % 60)) == 1 else f'0{self.segundos % 60}'
    return f'{int(self.segundos / 60)}:{segundos}'

  def tornar_musica_historica(self):
    self._historica = True
    Musica.musicas.update({self: self.__str__()})
  
  @classmethod
  def listar_musicas(cls):
    return '\n\n'.join(list(cls.musicas.values())) + '\n'
  