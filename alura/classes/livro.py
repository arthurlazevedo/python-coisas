from utils import capitalizar_condicional as capitalize

class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
    self._titulo = ' '.join(list(map(capitalize, titulo.split())))
    self._autor = autor
    self._ano_publicacao = ano_publicacao
    self._disponivel = True

  def __str__(self) -> str:
    return f'O livro {self.titulo} foi escrito por {self.autor} no ano de {self.ano_publicacao}'

  @property
  def emprestar(self):
    self._disponivel = False

  @property
  def titulo(self):
    return self._titulo
  
  @property
  def autor(self):
    return self._autor

  @property
  def ano_publicacao(self):
    return self._ano_publicacao
  
  @property
  def verificar_disponibilidade(self):
    return 'Disponível' if self._disponivel else 'Indisponível'


  #TODO: criar alguma classe para linkar com pessoa, aí criar um atributo em pessoa que represente essa classe
  # talvez uma família? composta por pessoa. Mas aí para isso teria que ter uma verificação muito grande 
  # que faria com que quando você atualizasse uma pessoa, fosse atualizado lá também, como definir os membros da família?

if __name__ == '__main__':
  print(list(map(capitalize, 'O rato roeu a roupa do rei de roma'.split())))