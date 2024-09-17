from utils import *

class Pessoa:
  pessoas = {}

  def __init__(self, nome: str, idade: int, profissao: str = 'sem emprego', genero: str = 'não binário'):
    self._nome = nome.title()
    self._idade = idade
    self._genero = genero.lower()
    self._profissao = ' '.join(list(map(capitalizar_condicional, profissao.split())))
    Pessoa.pessoas[self] = self.__str__

  def __str__(self):
    pronome = 'uma' if self.genero == 'mulher' else 'um' if self.genero == 'homem' else 'ume'
    anos = 'anos' if self.idade > 1 else 'ano'
    return f'{self.nome} é {pronome} {self.genero.lower()} de {self.idade} {anos}. Sua profissão é {self.profissao}'
  
  def aniversario(self):
    self.idade += 1
    Pessoa.pessoas.update({self: self.__str__()})

  @property
  def nome(self):
    return self._nome

  @property
  def idade(self):
    return self._idade
  
  @property
  def genero(self):
    return self._genero
  
  @property
  def profissao(self):
    return self._profissao
  
  @property
  def saudacao(self):
    pronome = 'uma' if self.genero == 'mulher' else 'um' if self.genero == 'homem' else 'ume'
    anos = 'anos' if self.idade > 1 else 'ano'
    final = f'Trabalho como {self.profissao}' if self.profissao != 'Sem Emprego' else 'Atualmente estou sem emprego'
    return f'Olá, meu nome é {self.nome}, sou {pronome} {self.genero.lower()} de {self.idade} {anos}. {final}'
  
  @property
  def funcao_exemplo():
    soma_notas = sum(avaliacoes['nota'] for avaliacoes in poggers)
    return soma_notas #desenvolver algo melhor aqui, juntar com a outra classe que faça sentido lá em cima. Acho que expandir no emprego talvez fosse bom.

  def listar_pessoas(cls):
    return '\n\n'.join(list(cls.pessoas.values()))