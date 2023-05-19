import pygame
import random

# Inicializar el juego
pygame.init()

# Definir las dimensiones de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Buscaminas")

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Definir las dimensiones de los bloques
block_size = 40
block_padding = 5

# Definir las dimensiones del tablero
board_width = 10
board_height = 10

# Calcular el tamaño total del tablero
board_total_width = (block_size + block_padding) * board_width
board_total_height = (block_size + block_padding) * board_height

# Definir la posición del tablero en la pantalla
board_x = (screen_width - board_total_width) // 2
board_y = (screen_height - board_total_height) // 2

# Definir la fuente del texto
font = pygame.font.Font(None, 30)

# Crear el tablero
board = [[0] * board_width for _ in range(board_height)]
mines = 10

# Colocar las minas aleatoriamente en el tablero
mines_coordinates = []
for _ in range(mines):
    while True:
        row = random.randint(0, board_height - 1)
        col = random.randint(0, board_width - 1)
        if (row, col) not in mines_coordinates:
            mines_coordinates.append((row, col))
            break

# Calcular el número de minas adyacentes para cada casilla vacía
for row in range(board_height):
    for col in range(board_width):
        if (row, col) not in mines_coordinates:
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < board_height and 0 <= col + j < board_width:
                        if (row + i, col + j) in mines_coordinates:
                            count += 1
            board[row][col] = count

# Crear una matriz para almacenar si cada casilla ha sido revelada o no
revealed = [[False] * board_width for _ in range(board_height)]

# Variable para almacenar el puntaje
score = 0

# Variable para indicar si se ha perdido
game_over = False

# Función para revelar una casilla y sus vecinas
def reveal(row, col):
    global score, game_over
    if 0 <= row < board_height and 0 <= col < board_width and not revealed[row][col]:
        revealed[row][col] = True
        if (row, col) in mines_coordinates:
            game_over = True
        elif board[row][col] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    reveal(row + i, col + j)
        else:
            score += 1

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over and event.button == 1:  # Clic izquierdo
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if board_x <= mouse_x < board_x + board_total_width and board_y <= mouse_y < board_y + board_total_height:
                    col = (mouse_x - board_x) // (block_size + block_padding)
                    row = (mouse_y - board_y) // (block_size + block_padding)
                    reveal(row, col)

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar el tablero
    for row in range(board_height):
        for col in range(board_width):
            x = board_x + col * (block_size + block_padding)
            y = board_y + row * (block_size + block_padding)
            if revealed[row][col]:
                pygame.draw.rect(screen, GRAY, (x, y, block_size, block_size))
                if board[row][col] != 0:
                    text = font.render(str(board[row][col]), True, WHITE)
                    text_rect = text.get_rect(center=(x + block_size // 2, y + block_size // 2))
                    screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, WHITE, (x, y, block_size, block_size))

    # Mostrar el puntaje
    score_text = font.render("Puntaje: " + str(score), True, WHITE)
    screen.blit(score_text, (20, 20))

    # Mostrar mensaje de fin de juego si se ha perdido
    if game_over:
        game_over_text = font.render("¡Has perdido!", True, WHITE)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.topleft = (20 + score_text.get_width() + 10, 20)
        screen.blit(game_over_text, game_over_rect)

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar el juego
pygame.quit()
