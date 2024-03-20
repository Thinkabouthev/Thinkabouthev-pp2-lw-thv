import pygame
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (225, 225, 225)
BLUE = (103, 235, 158)


BUTTON_SIZE = 60

game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Spotify')
BG_IMAGE_PATH = 'img/bg-mp7.png'
ICON_IMAGE_PATH = 'img/icon.png'
bg_image = pygame.image.load(os.path.normpath(BG_IMAGE_PATH))
pygame_icon = pygame.image.load(os.path.normpath(ICON_IMAGE_PATH))
pygame.display.set_icon(pygame_icon)

# Определение центральных координат для размещения фона
bg_x = SCREEN_WIDTH - 835
bg_y = 0

PLAY_IMAGE_PATH = 'img/play.png'
PAUSE_IMAGE_PATH = 'img/pause.png'
play_button = pygame.transform.scale(pygame.image.load(PLAY_IMAGE_PATH), (BUTTON_SIZE, BUTTON_SIZE))
pause_button = pygame.transform.scale(pygame.image.load(PAUSE_IMAGE_PATH), (BUTTON_SIZE, BUTTON_SIZE))

current_song_index = 0
SONGS = ['music/music1.mp3', 'music/music2.mp3', 'music/music3.mp3', 'music/music4.mp3', 'music/music5.mp3']
pygame.mixer.music.load(os.path.normpath(SONGS[current_song_index]))
pygame.mixer.music.play()

COVERS = ['img/cover/11.jpg', 'img/cover/22.jpg', 'img/cover/33.jpg', 'img/cover/44.jpg', 'img/cover/55.jpg']
ALBUM_COVER_SIZE = 250
album_cover = pygame.transform.scale(pygame.image.load(os.path.normpath(COVERS[current_song_index])), (ALBUM_COVER_SIZE, ALBUM_COVER_SIZE))

play = True
x = 0
font = pygame.font.SysFont('arialполужирный', 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        play = not play
        if play:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    
    if pressed[pygame.K_LEFT]: 
        current_song_index = (current_song_index - 1) % len(SONGS)
        pygame.mixer.music.load(SONGS[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        album_cover = pygame.transform.scale(pygame.image.load(COVERS[current_song_index]), (ALBUM_COVER_SIZE, ALBUM_COVER_SIZE))
            
    if pressed[pygame.K_RIGHT]: 
        current_song_index = (current_song_index + 1) % len(SONGS)
        pygame.mixer.music.load(SONGS[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        album_cover = pygame.transform.scale(pygame.image.load(COVERS[current_song_index]), (ALBUM_COVER_SIZE, ALBUM_COVER_SIZE))
        

    game_display.fill(WHITE)    
    game_display.blit(bg_image, (bg_x, bg_y))
    text = font.render(SONGS[current_song_index][6:-4], True, BLACK)
    game_display.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    game_display.blit(album_cover, (SCREEN_WIDTH // 2 - ALBUM_COVER_SIZE // 2, 65))
    
    pygame.draw.rect(game_display, LIGHT_GREEN, (SCREEN_WIDTH // 2 - ALBUM_COVER_SIZE // 2, 342, ALBUM_COVER_SIZE, 11))
    if play:
        x += 0.1
        if x > ALBUM_COVER_SIZE:
            x = 0
    pygame.draw.rect(game_display, BLUE, (SCREEN_WIDTH // 2 - ALBUM_COVER_SIZE // 2, 342, x, 11))
    
    BUTTON_X = 367
    BUTTON_Y = SCREEN_WIDTH - 350

    if play:
        game_display.blit(pause_button, (BUTTON_X, BUTTON_Y))
    else:
        game_display.blit(play_button, (BUTTON_X, BUTTON_Y))
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()
