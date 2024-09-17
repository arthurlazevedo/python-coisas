from colorama import Fore as fore
from pwinput import pwinput
from re import *

def formatar_cor(texto: str, tipo: str) -> str:
  match tipo:
    case 'warning_input':
      return input(f'{fore.RED}{texto}{fore.RESET}')
    case 'warning_pwinput':
      return pwinput(f'{fore.RED}{texto}{fore.RESET}')
    case 'warning_print':
      return print(f'{fore.RED}{texto}{fore.RESET}')
    case 'win_print':
      return print(f'{fore.GREEN}{texto}{fore.RESET}')

def exibir_erro(texto: str = '', tipo = '', warning = 'warning_input', fin = 0, texto_aviso = '', palpite = ''):
  
  genero = 'a' if tipo == 'Palavra' or 'Opção' else 'o'
  texto_aviso = (f'{tipo} inválid{genero}' if not texto_aviso else texto_aviso) + ', tente novamente: '

  match tipo:
    case 'Palavra' | 'Tema':
      while search('\d', texto) or len(texto) < 2 or (tipo == 'Palavra' and texto.__contains__('_')) or not search('\w', texto):
        texto = formatar_cor(texto_aviso, warning)
      return texto
    case 'Opção':
      while int_seguro(texto) < 1 or int_seguro(texto) > fin:
        texto = formatar_cor(texto_aviso, warning)
      return int(texto)
    case '_dica' | '_revelar':
      palpite = tipo if not palpite else palpite
      while palpite.lower() == tipo:
        palpite  = formatar_cor(texto_aviso, warning)
      return palpite

def contem_com_fore(palpite: str, lista: list):
  return lista.__contains__(f'{fore.RED}{palpite}{fore.RESET}') or lista.__contains__(f'{fore.GREEN}{palpite}{fore.RESET}') or lista.__contains__(f'{fore.YELLOW}{palpite}{fore.RESET}')

def int_seguro(num: str):
  if not num.isnumeric():
    return 0
  else:
    return int(num)
  
def split_verificado(palavra: str):
  return palavra.replace('-', ' ').split()

def index_seguro(palavra: str, idx: int):
  if len(palavra) - 1 < idx:
    return ''
  return palavra[idx]

def converter_sn(resposta: str):
  return '1' if resposta.lower() == 's' else '2' if resposta.lower() == 'n' else '0'

def desconsiderar_especial(texto: str):
  contador = 0
  while not texto.isascii() and contador <= 5:
    texto = retirar_formatacao(texto, contador)
    contador += 1

  return texto

def retirar_formatacao(texto: str, num: int):
    match num:
      case 0:
        texto = sub('[âãáà]', 'a', texto)
      case 1:
        texto = texto.replace('ç', 'c')
      case 2:
        texto = sub('[êé]', 'e', texto)
      case 3:
        texto = sub('[ôó]', 'o', texto)
      case 4:
        texto = texto.replace('í', 'i')
      case 5:
        texto = texto.replace('ú', 'u')
    return texto

if __name__ == "__main__":
  print(type('ú'))