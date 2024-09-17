from typing import List
from livro import Livro
from utils import capitalizar_condicional

class Bibilioteca:
  def __init__(self, nome: str, localizacao: str):
    self._nome = ' '.join(list(map(capitalizar_condicional, nome.split())))
    self._localizacao = ' '.join(list(map(capitalizar_condicional, localizacao.split())))
    self._livros: List[Livro] = []
  
  def __str__(self):
    return f'A {self.biblioteca} fica cidade de {self.localizacao}. Ela possui {self.qtd_livros} livros em seu repertório.'

  @property
  def cadastrar_livro(self, titulo, autor, ano_publicacao):
    self._livros.append(Livro(titulo, autor, ano_publicacao))
    return 'Livro cadastrado com sucesso!'

  @property
  def emprestar_livro(self, titulo_livro):
    for livro in self._livros:
      if livro.titulo == titulo_livro:
        if livro.verificar_disponibilidade:
          livro.emprestar
          return 'Tome'
        else:
          return 'Livro indisponível'

  @property
  def qtd_livros(self):
    return len(self.livros)

  @property
  def nome(self):
    return self._nome
  
  @property
  def localizacao(self):
    return self._localizacao
  
  @property
  def livros(self):
    return self._livros
  