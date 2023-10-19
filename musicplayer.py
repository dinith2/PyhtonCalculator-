import pygame
import random

pygame.init()

window = pygame.display.set_mode((400, 200))

music_files = [
    "music_file_1.mp3",
    "music_file_2.mp3",
    "music_file_3.mp3",
    "music_file_4.mp3",
    "music_file_5.mp3",
]


random.shuffle(music_files)

current_track = 0

pygame.mixer.music.load(music_files[current_track])

pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pygame.mixer.music.get_busy():
        current_track += 1
        if current_track >= len(music_files):
            current_track = 0  
        pygame.mixer.music.load(music_files[current_track])
        pygame.mixer.music.play()

pygame.quit()
 