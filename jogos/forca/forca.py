from os import system
from re import search, sub
from colorama import Fore as fore
from random import randrange
from pwinput import pwinput
from utilitarios import *
from mensagens import *

def forca_introducao(enforcado = None, enforcador = None):
  print(aplicacao, '\n')
  
  if (not enforcado):
    enforcador = input('Digite seu nome, enforcador: ')
    enforcado = input('Digite seu nome, enforcado: ')
    while enforcado == enforcador:
      formatar_cor('Enforcado e enforcador não podem ter o mesmo nome. ', 'warning_print')
      enforcador = formatar_cor('Nome do enforcador: ', 'warning_input')
      enforcado = formatar_cor('Nome do enforcado: ', 'warning_input')
    system('clear')
    print(modo_especial(enforcador, enforcado))
  else:
    print(mensagem_tipo_jogos)

  tipo_jogo = exibir_erro(input('\n' + '\n'.join(opcoes_modo_especial) + '\n\nEscolha a opção: '), 'Opção', fin = 4)
  system('clear')

  print('Vocês escolheram a opção \033[1m' + opcoes_modo_especial[tipo_jogo - 1] + '\033[0m!')
  
  palavra = exibir_erro(pwinput(f'{enforcador}, digite a palavra que deve ser adivinhada: '), 'Palavra', 'warning_pwinput')
  tema = exibir_erro(input(f'{enforcador}, qual o tema da palavra? '), 'Tema')

  dica = ''
  roleta_russa = False
  match int(tipo_jogo):
    case 1:
      dica = pwinput(f'{enforcador}, digite a dica para {enforcado}: ')
      roleta_russa = True
    case 2:
      dica = pwinput(f'{enforcador}, digite a dica para {enforcado}: ')
    case 3:
      roleta_russa = True

  return {
    'roleta_russa': roleta_russa,
    'enforcador': enforcador,
    'enforcado': enforcado,
    'palavra': palavra,
    'tema': tema,
    'dica': dica
  }

def forca_informacoes(infos: dict, palavra_escondida: str, tentativas: int, letras: list, chutes: list, mostrar_dica: bool, ja_usado: bool):
  system('clear')

  tema = infos['tema']
  dica = infos['dica']

  print(f'\033[1mO tema é {tema}! \033[0m')

  print(enforcado_formas[f'forma_{tentativas}'], '\n')
  
  palavra_escondida = palavra_escondida.replace('', ' ')
  print(f'Palavra: {palavra_escondida}\n')

  if mostrar_dica:
    print(f'\033[1mA dica dada foi: {dica}\033[0m')
  elif dica and tentativas >= 3:
    print(f'\033[1mVocê já pode usar sua dica (_dica)!\033[0m')
  if infos.get('roleta_russa') and not ja_usado:
    print(f'\033[1mVocê pode revelar uma letra (_revelar)!\033[0m')

  print('')

  letras = ', '.join(letras)
  chutes = ', '.join(chutes)
  print(f'Letras já tentadas: {letras}')
  print(f'Chutes atuais: {chutes}\n')

def forca_saida(saida: str, enforcado: str, enforcador: str, palavra: str):
  system('clear')
  
  match saida:
    case 'vitória':
      print(enforcado_ganhou)
      mensagem_final(palavra, f'\n{enforcador}, mais sorte na próxima!', fore.GREEN)
    case 'derrota':
      print(enforcado_perdeu)
      mensagem_final(palavra, f'\nInfelizmente você foi incapaz, {enforcado} :(', fore.RED)
  
  jogar_dnv = exibir_erro(converter_sn(input('Gostariam de jogar novamente? [S/n]').strip()), 'Opção', fin = 2)
  
  system('clear')

  if jogar_dnv == 1:
    print('1. Com os mesmos jogadores;\n2. Funções trocadas;\n3. Com jogadores diferentes\n')

    forma_jogo = exibir_erro(input('Escolha a forma de jogo: '), 'Opção', fin = 3)
    
    match int(forma_jogo):
      case 1:
        forca(enforcado, enforcador)
      case 2:
        forca(enforcador, enforcado)
      case 3:
        forca()
  else:
    system('clear')
    print('Fechando o programa...')

def forca_jogo(infos: dict, palavra_escondida: str):
  tentativas = 0
  letras = []
  chutes = []
  palavra: str = infos['palavra']
  palavra_formatada = desconsiderar_especial(palavra).lower()
  palavras_sep = split_verificado(palavra_formatada)
  letras_da_palavra = list(palavra_escondida)
  mostrar_dica = False
  ja_foi_aleatorio = False
  
  while palavra_escondida.__contains__('_') and tentativas < 6:
    forca_informacoes(infos, palavra_escondida, tentativas, letras, chutes, mostrar_dica, ja_foi_aleatorio)

    palpite = desconsiderar_especial(input('Faça seu palpite (letra/palavra): ')).lower()
    while len(palpite) < 1 or search('\d', palpite) or contem_com_fore(palpite, letras) or contem_com_fore(palpite, chutes):
      palpite = desconsiderar_especial(formatar_cor('Palpite inválido, digite novamente: ', 'warning_input')).lower()

    eh_comando = False
    sair = False
    while palpite.startswith('_') and not sair:
      eh_comando = True
      if (palpite.lower() == '_dica' and not infos['dica']) or (palpite.lower() == '_revelar' and not infos['roleta_russa']):
        palpite = exibir_erro(tipo = palpite.lower(), texto_aviso = 'Essa opção não foi ativada', palpite = palpite)
        eh_comando = False
      elif palpite.lower() == '_dica':
        if tentativas < 4:
          palpite = exibir_erro(tipo = '_dica', texto_aviso = 'A dica ainda não pode ser acessada')
          eh_comando = False
        elif mostrar_dica:
          palpite = exibir_erro(tipo = '_dica', texto_aviso = 'A dica já foi utilizada')
          eh_comando = False
        else:
          sair = True
          mostrar_dica = True
          tentativas += 1
      elif palpite.lower() == '_revelar':
        if ja_foi_aleatorio:
          palpite = exibir_erro(tipo = '_revelar', texto_aviso = 'Você já usou seu revelar')
          eh_comando = False
        else:
          roleta = randrange(0, len(palavra_formatada), 1)
          while contem_com_fore(palavra_formatada[roleta], letras) and not search('\w', palavra_formatada[roleta]):
            roleta = randrange(0, len(palavra_formatada), 1)
          for idx_seq in range(0, len(palavra), 1):
            if palavra_formatada[idx_seq] == palavra_formatada[roleta]:
              letras_da_palavra[idx_seq] = palavra[idx_seq]
          ja_foi_aleatorio = True
          sair = True
          palavra_escondida = ''.join(letras_da_palavra)
          letras.append(f'{fore.YELLOW}{palavra_formatada[roleta]}{fore.RESET}')
          tentativas += 1
      else:
        while palpite.startswith('_'):
          palpite = formatar_cor('Comando inválido, tente novamente: ', 'warning_input')
        eh_comando = False

    acertou_mizeravi = False
    if not eh_comando:
      if len(palpite) > 1:
        if palpite.lower().replace('-', ' ') == palavra_formatada.lower().replace('-', ' '):
          palavra_escondida = palavra
        elif palavras_sep.__contains__(palpite):
          for palavra_solo in palavras_sep:
            for idx_p in range(0, len(palavra_solo), 1):
              if palavra_solo[idx_p].lower() == index_seguro(palpite, idx_p).lower():
                letras_da_palavra[idx_p + palavra_formatada.index(palavra_solo)] = palavra[idx_p + palavra_formatada.index(palavra_solo)]
          palavra_escondida = ''.join(letras_da_palavra)
          chutes.append(f'{fore.GREEN}{palpite}{fore.RESET}')
        else:
          chutes.append(f'{fore.RED}{palpite}{fore.RESET}')
          tentativas += 1
      else:
        if palavra_formatada.__contains__(palpite):
          acertou_mizeravi = True
          for idx in range(0, len(palavra), 1):
            if palavra_formatada[idx].lower() == palpite:
              letras_da_palavra[idx] = palavra[idx]
          palavra_escondida = ''.join(letras_da_palavra)
        else:
          tentativas += 1
        
        letras.append(f'{fore.GREEN if acertou_mizeravi else fore.RED}{palpite}{fore.RESET}')
  
  tipo_mensagem = 'derrota' if tentativas > 5 else 'vitória'

  forca_saida(tipo_mensagem, infos['enforcado'], infos['enforcador'], palavra.upper())

def forca(enforcado = None, enforcador = None):
  try:
    system('clear')

    forca_atual = forca_introducao(enforcado, enforcador)
    palavra_escondida = sub('\w', '_', forca_atual['palavra'])

    forca_jogo(forca_atual, palavra_escondida)

  except KeyboardInterrupt:
    system('clear')

if __name__ == '__main__':
  forca()