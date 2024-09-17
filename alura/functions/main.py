from os import system
import funcoes as funcoes

def opcoes():
  print('''------ OPÇÕES -------
1. Checar se um número é par
2. Determinar sua faixa de idade
3. Confirmar seu usuário e senha
4. Determinar o quadrante dos números
5. Determinar quantas vezes uma palavra se repete em uma string
6. Fechar o programa\n''')
  
  try:
    return int(input('Escolha a opção: '))
  except:
    return 0

def escolher_opcao(opcao):
  system('clear')
  match opcao:
    case 1:
      funcoes.eh_par()
    case 2:
      funcoes.determina_faixa()
    case 3:
      funcoes.eh_dos_meus()
    case 4:
      funcoes.qual_quadrante()
    case 5:
      funcoes.contar_ocorrencias()
    case 6:
      print('Encerrando a aplicação...')
    case 0:
      input('Opção inválida, reinicie a aplicação com enter')
      iniciar_aplicacao()

def iniciar_aplicacao():
  system('clear')
  escolher_opcao(opcoes())

if __name__ == '__main__':
  iniciar_aplicacao()