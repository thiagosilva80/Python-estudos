import pygame
from pathlib import Path

pygame.init()

arquivo = Path(__file__).parent / 'ex014.mp3'

pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()

input('Pressione Enter para encerrar...')

