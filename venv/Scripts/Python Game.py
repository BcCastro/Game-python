import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva los Obstáculos")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10

obstacle_size = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

clock = pygame.time.Clock()

# Función para dibujar al jugador
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

# Función para dibujar los obstáculos
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

# Función para mostrar el menú de inicio
def show_start_menu():
    font = pygame.font.Font(None, 36)
    text = font.render("Presiona SPACE para empezar", True, WHITE)
    screen.blit(text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Función para mostrar el menú de fin de juego
def show_game_over_menu():
    font = pygame.font.Font(None, 36)
    text = font.render("¡Has perdido! Presiona R para reiniciar", True, WHITE)
    screen.blit(text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False
                restart_game()

# Función para reiniciar el juego
def restart_game():
    global player_x, obstacles
    player_x = WIDTH // 2 - player_size // 2
    obstacles = []

# Función principal del juego
def game():
    global player_x, obstacles

    show_start_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 5
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += 5

        if random.randrange(obstacle_frequency) == 0:
            obstacle_x = random.randrange(WIDTH - obstacle_size)
            obstacle_y = -obstacle_size
            obstacles.append([obstacle_x, obstacle_y, obstacle_size, obstacle_size])

        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > HEIGHT:
                obstacles.remove(obstacle)

        for obstacle in obstacles:
            if (
                player_x < obstacle[0] + obstacle[2]
                and player_x + player_size > obstacle[0]
                and player_y < obstacle[1] + obstacle[3]
                and player_y + player_size > obstacle[1]
            ):
                show_game_over_menu()

        screen.fill((0, 0, 0))
        draw_player(player_x, player_y)
        draw_obstacles(obstacles)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    game()
