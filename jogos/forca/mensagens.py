from colorama import Fore as fore

aplicacao = '''
███████╗ ██████╗ ██████╗  ██████╗ █████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
█████╗  ██║   ██║██████╔╝██║     ███████║
██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║
██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝'''

mensagem_tipo_jogos = 'Gostariam de jogar com as opções de dica e revelar?'

def modo_especial(enforcador: str, enforcado: str): 
  return f'''{mensagem_tipo_jogos}

Dica: {enforcador} escreverá uma dica secreta para {enforcado}, que só pode ser acessada quando restar duas tentativas, usar 
a dica {fore.RED}custará uma tentativa{fore.RESET}. Para usar a dica, digite \033[1m{fore.BLUE}_dica{fore.RESET}\033[0m

Revelar: {enforcado}, uma vez durante o jogo você pode digitar \033[1m{fore.BLUE}_revelar{fore.RESET}\033[0m para revelar todas 
as ocorrências de uma letra aleatória da palavra, usar esse comando {fore.RED}também lhe custará uma tentativa{fore.RESET}

{enforcado}, note que, caso use dica/revelar quando estiver com 5 tentativas, você \033[1m{fore.RED}perderá automaticamente{fore.RESET}\033[0m'''

opcoes_modo_especial = [
  '1. Jogar com ambos',
  '2. Jogar apenas com dicas',
  '3. Jogar apenas com revelar',
  '4. Jogar sem nenhum'
]

enforcado_formas = {
  'forma_0': '''  ___________
 |/          ┆
 |           ┆
 |          
 |          
 |
 |
 |
_|_ ''',
  'forma_1': '''  ___________
 |/          ┆
 |           ┆
 |         (•᎑•)
 |          
 |
 |
 |
_|_''',
  'forma_2': '''  ___________
 |/          ┆ 
 |           ┆ 
 |         (•᎑•)
 |           |
 |           |
 |
 |
_|_''',
  'forma_3': '''  ___________
 |/          ┆ 
 |           ┆ 
 |         (•᎑•)
 |          /|
 |           |
 |	    
 |
_|_''',
  'forma_4': '''  ___________
 |/          ┆ 
 |           ┆ 
 |         (•᎑•)
 |          /|\\
 |           |
 |	    
 |
_|_''',
  'forma_5': '''  ___________
 |/          ┆ 
 |           ┆ 
 |         (•᎑•)
 |          /|\\
 |           |
 |          /
 |
_|_'''
}

enforcado_ganhou = '''
              ██████╗  █████╗ ██████╗  █████╗ ██████╗ ███████╗███╗   ██╗███████╗       ██╗   ██╗ ██████╗  ██████╗███████╗     ██████╗  █████╗ ███╗   ██╗██╗  ██╗ ██████╗ ██╗   ██╗██╗
ᕙ(•̀ ᗜ •́ )ᕗ    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝       ██║   ██║██╔═══██╗██╔════╝██╔════╝    ██╔════╝ ██╔══██╗████╗  ██║██║  ██║██╔═══██╗██║   ██║██║
    |         ██████╔╝███████║██████╔╝███████║██████╔╝█████╗  ██╔██╗ ██║███████╗       ██║   ██║██║   ██║██║     █████╗      ██║  ███╗███████║██╔██╗ ██║███████║██║   ██║██║   ██║██║
    |         ██╔═══╝ ██╔══██║██╔══██╗██╔══██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║       ╚██╗ ██╔╝██║   ██║██║     ██╔══╝      ██║   ██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██║   ██║╚═╝
   / \\        ██║     ██║  ██║██║  ██║██║  ██║██████╔╝███████╗██║ ╚████║███████║▄█╗     ╚████╔╝ ╚██████╔╝╚██████╗███████╗    ╚██████╔╝██║  ██║██║ ╚████║██║  ██║╚██████╔╝╚██████╔╝██╗
              ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝      ╚═══╝   ╚═════╝  ╚═════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝'''

enforcado_perdeu = '''
  ___________
 |/          ┆
 |           ┆         ██████╗ ██╗   ██╗███████╗    ██████╗ ███████╗███╗   ██╗ █████╗        ██╗   ██╗ ██████╗  ██████╗███████╗    ██████╗ ███████╗██████╗ ██████╗ ███████╗██╗   ██╗        ██╗
 |         (x_x)      ██╔═══██╗██║   ██║██╔════╝    ██╔══██╗██╔════╝████╗  ██║██╔══██╗       ██║   ██║██╔═══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║    ██╗██╔╝
 |          /|\\       ██║   ██║██║   ██║█████╗      ██████╔╝█████╗  ██╔██╗ ██║███████║       ██║   ██║██║   ██║██║     █████╗      ██████╔╝█████╗  ██████╔╝██║  ██║█████╗  ██║   ██║    ╚═╝██║ 
 |           |        ██║▄▄ ██║██║   ██║██╔══╝      ██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║       ╚██╗ ██╔╝██║   ██║██║     ██╔══╝      ██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██╔══╝  ██║   ██║    ██╗██║ 
 |          / \\       ╚██████╔╝╚██████╔╝███████╗    ██║     ███████╗██║ ╚████║██║  ██║▄█╗     ╚████╔╝ ╚██████╔╝╚██████╗███████╗    ██║     ███████╗██║  ██║██████╔╝███████╗╚██████╔╝    ╚═╝╚██╗
 |                     ╚══▀▀═╝  ╚═════╝ ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝      ╚═══╝   ╚═════╝  ╚═════╝╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝         ╚═╝
_|_'''

def mensagem_final(palavra: str, mensagem: str, fore_cor):
  print(f'\n\033[1m {fore_cor}A PALAVRA ERA {palavra}!{fore.RESET} \033[0m')
  print(mensagem, '\n')

if __name__ == '__main__':
  print(enforcado_formas['forma_0'])
  print(enforcado_formas['forma_1'])
  print(enforcado_formas['forma_2']) 
  print(enforcado_formas['forma_3'])
  print(enforcado_formas['forma_4'])
  print(enforcado_formas['forma_5'])