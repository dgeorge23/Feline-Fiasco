import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("mixkit-driving-in-the-rain-1242.wav")  # Replace "audio.wav" with the path to your audio file

pygame.mixer.music.play()  # This will start playing the audio file

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Your game logic goes here
    
pygame.quit()
