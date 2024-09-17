from os import system
from musica import Musica

nova_musica = Musica('Everybody wants to Rule the World', 1985, 'Tears for Fears', 251)
outra_musica = Musica('Maps', 2014, 'Maroon 5', 189)

nova_musica.tornar_musica_historica()

if __name__ == '__main__':
  system('clear')
  print(Musica.listar_musicas())