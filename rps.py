import pygame
import random
# Start Pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
PINK = (255, 192, 203)
BLUE = (0, 0, 255)


#Font
font = pygame.font.SysFont(None, 60)

#Choices
choices = ["rock", "paper", "scissors"]

# Scores
player_score = 0
computer_score = 0

class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, PINK, self.rect)
        text_surface = font.render(self.text, True, BLUE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface,(self.rect.x+20, self.rect.y+20))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    rock_button = Button("Rock", 50, 450, 200, 100)
    paper_button = Button("Paper", 300, 450, 200, 100)
    scissors_button = Button("Scissors", 550, 450, 200, 100)

    # Game Loops
    running=True
    
    player_choice=""
    computer_choice=""
    result=""