#Подключаем библиотек для создания игры
import pygame

#Инизализируем модуль игры
pygame.init()

#Настройки экрана
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Chess Game')

font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)


#Выходим из модуля игры
pygame.quit()