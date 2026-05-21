
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
BG_COLOR = (100, 150, 200)

# Font
font = pygame.font.SysFont(None, 60)

# Choices
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

        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Create buttons
rock_button = Button("Rock", 50, 450, 200, 100)
paper_button = Button("Paper", 300, 450, 200, 100)
scissors_button = Button("Scissors", 550, 450, 200, 100)

# Game loop
running = True

player_choice = ""
computer_choice = ""
result = ""

while running:

    # Background color
    screen.fill(BG_COLOR)

    # Draw buttons
    rock_button.draw()
    paper_button.draw()
    scissors_button.draw()

    # Show text
    player_text = font.render(f"Player: {player_score}", True, BLUE)
    computer_text = font.render(f"Computer: {computer_score}", True, BLUE)
    result_text = font.render(result, True, BLUE)

    screen.blit(player_text, (50, 50))
    screen.blit(computer_text, (50, 120))
    screen.blit(result_text, (200, 300))

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            # Player choice
            if rock_button.is_clicked(mouse_pos):
                player_choice = "rock"

            elif paper_button.is_clicked(mouse_pos):
                player_choice = "paper"

            elif scissors_button.is_clicked(mouse_pos):
                player_choice = "scissors"

            # Computer choice
            if player_choice:
                computer_choice = random.choice(choices)

                # Determine winner
                if player_choice == computer_choice:
                    result = "DRAW!"

                elif (
                    (player_choice == "rock" and computer_choice == "scissors")
                    or (player_choice == "paper" and computer_choice == "rock")
                    or (player_choice == "scissors" and computer_choice == "paper")
                ):
                    result = "You Win!"
                    player_score += 1

                else:
                    result = "Computer Wins!"
                    computer_score += 1

                # Reset choice
                player_choice = ""

    pygame.display.update()

pygame.quit()