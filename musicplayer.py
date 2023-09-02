import pygame

pygame.init()

window = pygame.display.set_mode((400, 200))

# Load your music file
pygame.mixer.music.load("your_music_file.mp3")

# Start playing the music
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.mixer.music.stop()

pygame.quit()
