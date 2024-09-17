#Python

##Geral:

- print() => printa no console a informação
- input() => printa no console e retorna o que o usuário respondeu
- vars(arg?) => mesmo que locals quando não tem argumento, se não retorna o mesmo que objeto.__dict__ (variáveis do objeto ou algo do tipo)
- locals() => retorna informações do arquivo e suas variáveis/funções
- dir(arg?) => uma lista com as chaves de locals sem argumento, com argumento retorna lista das propriedades do objeto => instâncias de classe, variáveis... 

- vars e locals retornam dicionários, enquanto que dir retorna uma lista.

- __name__ => o nome do arquivo, quando é executado ele é sempre '__main__' => não pode ser importado

- As pastas na importação são acessadas através de pontos => pasta_1.pasta_2.arquivo
  - Não é necessário 'sair' (../) da pasta no import para acessar outras pastas
  - Pode ser importado dessa maneira: from arquivo import funcao/variavel

###Imports muito comuns:

os => parece ter várias coisas relacionadas a terminal(system('comando') é o que eu mais uso)
re => lida com regex
colorama = até onde vi, lida com coloração no terminal
getpass => tem uma funcao getpass para input escondido

##Declaração

- As variáveis são definidas sem palavra chave (como let ou const), só precisa botar o nome
- Funções são definidas com 'def'
- Utiliza snake_case

##Condicionais:

- Ao invés de utilizar && e ||, se utiliza and e or.
- Não é necessário usar and para operações como 3 < 5 < 4
- Ao invés de utilizar !variável, se utiliza not variável

###If/Else: if => elif => else

Exemplo: 
  if 1 == 1: print('uau')
  elif 2 == 2: print('pog')
  else: print('hmm')

###Ternários: valor_1 if condicao else valor_2

Exemplo:
  opcao = 1 if 1 == 1 else 2

###Switch: match => case => case _

Exemplo:
  match opcao:
    case 1:
      'a'
    case 2 | c:
      'b'
    case _:
      'padrão'

##Conversão

- int(valor)
- bool(valor)
- str(valor)

##Tuplas e Listas

- Python possui tuplas (não podem ser alteradas, são definidas com tamanho e conteúdo fixo) => processamento melhor. (1, 2, 3)
- Listas são arrays normais que não possuem tipo definido, assim como em javascript => [1, 2, 3, 4, 5]

##For e While

- Usar in para iterar por listas/tuplas, talvez of para objetos? Tem como aparentemente fazer for _ in range(numero), entender melhor essa função
  
  - For => range(numInicial, numFinal, numAdicionar) => (1, 11, 2), (10, 0, -1) 
    numInicial: valor inicial da variável
    numFinal: valor até onde a variável pode alcançar - 1 (se 11, chega até 10)
    numAdicionar: valor que será adicionado/subtraído da variável sempre que for feita uma iteração

- While é basicamente a mesma estrutura de sempre

##Dicionário

- {
  'chave': valor
}

- Basicamente Map em Java/Objeto em JavaScript

- Para pegar a propriedade: dicionario['chave']
- Para setar uma propriedade: dicionario['chave'] = valor => ou com dicionario.update({'chave': valor})
- Para adicionar/atualizar uma chave com valor default: dicionario['chave'] = dicionario.get('chave', default)

##Classes

- Funcionam assim como classes em Java e Javascript
- O 'this' é comumente referido como self, mas não precisa ser esse nome obrigatoriamente
- O constructor daqui é a função __init__(self, ...vars) => def __init__(...):
- Com vars(instancia) ou instancia.__dict__, mostra os atributos da classe.
- __str__(self) é a representação textual do objeto, quando um objeto é printado ele irá mostrar o retorno dessa função

- Uma classe só vai possuir o atributo se você definir ele, com o __init__ apenas as instâncias da classe terão o atributo
  - por isso, usar getattr em uma classe sem variáveis, mas com construtor vai retornar erro.
  - ou até mesmo Classe.atributo, que funciona também

- Tem como deixar o atributo de uma classe "privado" => _atributo
  - Não torna privado, mas só significa visualmente que ele não deve ser acessado, mas ele pode sim ser

- @property => define um método get para um certo atributo (privado geralmente), ele pode ser acessado sem passar nada, só com instancia.property
 - @classmethod => define um método para a classe, não é necessário, mas é uma boa prática

FastAPI/Uvicorn

from fastapi import FastApi
funcao = FastApi()

rodar localmente:
uvicorn arquivo:funcao --reload --host(definir o host: localhost) --port (definir a porta, padrão é 8000)