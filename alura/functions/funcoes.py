def eh_par():
  '''
  - Checa se um número é par.
  - Input: Número a ser checado
  - Output: texto para caso o número seja par ou ímpar
  '''
  
  num = int(input('Escolha um número: '))

  if num % 2 == 0:
    print('O número é par!')
  else:
    print('O número é ímpar')

def determina_faixa():
  '''
  - Determina a faixa de idade de um usuário.
  - Input: Idade do usuário
  - Output: texto mostrando qual sua faixa de idade
  '''

  idade = int(input('Diga a sua idade: '))

  if idade < 0:
    print('pode não man')
  elif idade < 13:
    print('vai lá crianção')
  elif idade < 19:
    print('adolescente chato')
  else:
    print('ai meu deus eu já sou um adulto')

def eh_dos_meus():
  '''
  - Checa se o usuário e senha estão corretos.
  - Input: 
    - Usuário para ser checado
    - Senha para ser checada
  - Output: texto de sucesso ou erro
  '''
  
  usuario = input('Usuário: ')
  senha = input ('Senha: ')

  if usuario == 'tutu' and senha == 'tuzinho':
    print('é dos meus')
  else:
    print('ei man')

def qual_quadrante():
  '''
  - Checa qual o quadrante do ponto criado a partir dos números informados.
  - Input: 
    - X: posição do ponto no eixo x
    - Y: posição do ponto no eixo y
  - Output: mensagem definindo o quadrante do número
  '''
  
  x = int(input('Diga o valor de x: '))
  y = int(input('Diga o valor de y: '))

  if x > 0 and y > 0:
    print('primero')
  elif x < 0 < y:
    print('segundo')
  elif x < 0 and y < 0:
    print('tercero')
  elif y < 0 < x:
    print('cuarto')
  else:
    print('eixo/centro')

def contar_ocorrencias():
  '''
  - Conta ocorrências de uma palavra em um texto.
  - Input: Texto para ser checado
  - Output: texto informando a quantidade de vezes que uma palavra se repete
  '''
  
  frase = input('Digite a frase para verificar: ').split()
  print('')
  ocorrencias = {}

  for palavra in frase:
    ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1  
  for palavra in ocorrencias:
    print(f'A palavra {palavra} se repete {ocorrencias[palavra]} vez' + ('es' if ocorrencias[palavra] > 1 else ''))

if __name__ == '__main__':
  print('o rato roeu a roupa do rei de roma'.split())