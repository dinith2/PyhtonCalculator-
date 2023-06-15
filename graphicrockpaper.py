import pygame
import random

pygame.init()

win_width = 640
win_height = 480
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Rock-Paper-Scissors")

rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")
player_choices = [rock_img, paper_img, scissors_img]

running = True
clock = pygame.time.Clock()

player_choice = None
computer_choice = None

def get_computer_choice():
    return random.choice(player_choices)

def display_choices():
    global player_choice, computer_choice
    for i, choice in enumerate(player_choices):
        win.blit(choice, (i*200, win_height/2))
    if computer_choice is not None:
        win.blit(computer_choice, (win_width/2 - 50, 50))
    if player_choice is not None:
        win.blit(player_choice, (win_width/2 - 50, win_height - 150))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(player_choices)):
                choice_rect = player_choices[i].get_rect()
                choice_rect.x = i*200
                choice_rect.y = win_height/2
                if choice_rect.collidepoint(mouse_pos):
                    player_choice = player_choices[i]
                    computer_choice = get_computer_choice()

    win.fill((255, 255, 255))
    display_choices()
    pygame.display.update()

    clock.tick(60)

pygame.quit()