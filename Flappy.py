import pygame
from random import randint

pygame.init()
display_width = 640
display_height = 900
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Flappy Bird")
text = pygame.font.Font(None, 70)

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (display_width, display_height))

bird = pygame.image.load('bird.png')
bird = pygame.transform.scale(bird, (80, 80))

pole_width = 120
pole_gap = 200
pole_x = display_width
top_pole_height = randint(150, 600)
pole_color = (220, 85, 57)

bird_x = 50
bird_y = top_pole_height + 50
score = 0
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y -= 6
    elif keys[pygame.K_DOWN]:
        bird_y += 8

    display.blit(bg, (0, 0))
    display.blit(bird, (bird_x, bird_y))

    pole_x -= 7
    if pole_x <= -pole_width:
        pole_x = display_width
        top_pole_height = randint(100, 600)
        score += 20

    pygame.draw.rect(display, pole_color, (pole_x, 0, pole_width, top_pole_height))
    pygame.draw.rect(display, pole_color, (pole_x, top_pole_height + pole_gap, pole_width, display_height))

    # Collision detection
    bird_width = 80
    bird_height = 80
    if pole_x <= bird_x + bird_width and bird_x <= pole_x + pole_width:
        if bird_y <= top_pole_height or bird_y + bird_height >= top_pole_height + pole_gap:
            game_over = True

    score_text = text.render(f'Score: {score}', True, (255, 255, 255))
    display.blit(score_text, (20, 20))
    pygame.display.update()
    clock.tick(60)

# Game Over screen
display.blit(bg, (0, 0))
final_text = text.render("GAME OVER", True, (255, 0, 0))
final_score_text = text.render(f"Final Score: {score}", True, (255, 255, 255))
display.blit(final_text, (display_width//2 - 150, display_height//2 - 50))
display.blit(final_score_text, (display_width//2 - 200, display_height//2 + 50))
pygame.display.update()

pygame.time.wait(3000)
pygame.quit()
