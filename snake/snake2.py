import pygame
import random
import time
import psycopg2

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
INITIAL_FPS = 5  # Initial frames per second
FOOD_TIMER = 10  # Food timer in seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

class Snake:
    def __init__(self, fps):
        self.body = [(100, 100)]
        self.direction = (1, 0)
        self.fps = fps
        self.food_position = self.generate_food_position()
        self.food_weight = self.generate_food_weight()
        self.food_timer = time.time() + FOOD_TIMER
        self.score = 0
        self.level = 1

    def move(self):
        head = (self.body[0][0] + self.direction[0] * GRID_SIZE, self.body[0][1] + self.direction[1] * GRID_SIZE)
        # Wrap around the screen edges
        head = (head[0] % SCREEN_WIDTH, head[1] % SCREEN_HEIGHT)
        if head in self.body[1:]:
            return True  # Game over
        self.body.insert(0, head)
        if head[0] == self.food_position[0] and head[1] == self.food_position[1]:
            self.score += self.food_weight  # Increase score based on food weight
            if self.score % 3 == 0:
                self.level += 1
                self.fps += 1  # Increase FPS
            self.food_position = self.generate_food_position()
            self.food_weight = self.generate_food_weight()
            self.food_timer = time.time() + FOOD_TIMER  # Reset food timer
        else:
            self.body.pop()
        return False

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def generate_food_position(self):
        while True:
            x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
            if (x, y) not in self.body:
                return (x, y)

    def generate_food_weight(self):
        return random.choice([1, 2, 3, 5])  # Randomly select food weight from available options

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.snake = None
        self.game_over_font = pygame.font.Font(None, 48)
        self.db_conn = self.connect_to_db()

        # Create SNAKE_GAME table if not exists
        self.create_table()

        # Load food images and resize them
        self.food_images = {
            1: pygame.transform.scale(pygame.image.load('img/ap.png').convert_alpha(), (GRID_SIZE, GRID_SIZE)),
            2: pygame.transform.scale(pygame.image.load('img/berry.png').convert_alpha(), (GRID_SIZE, GRID_SIZE)),
            3: pygame.transform.scale(pygame.image.load('img/cherry.png').convert_alpha(), (GRID_SIZE, GRID_SIZE)),
            5: pygame.transform.scale(pygame.image.load('img/goldapple.png').convert_alpha(), (GRID_SIZE, GRID_SIZE)),
        }

    def connect_to_db(self):
        try:
            conn = psycopg2.connect(
                host='localhost',
                port=5432,
                database='pp2',
                user='postgres',
                password='dariko1102'
            )
            print("Connected to the database")
            return conn
        except psycopg2.Error as e:
            print("Error connecting to the database:", e)

    def create_table(self):
        try:
            cur = self.db_conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS SNAKE_GAME (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(30) NOT NULL UNIQUE,
                user_score INT,
                level INT
            );""")
            self.db_conn.commit()
            print("SNAKE_GAME table created successfully")
        except psycopg2.Error as e:
            print("Error creating SNAKE_GAME table:", e)

    def start(self):
        # Ask user for username
        username = input("Enter your username: ")
        self.load_user(username)

        if self.snake:
            self.run()

    def load_user(self, username):
        try:
            cur = self.db_conn.cursor()
            cur.execute("SELECT level FROM SNAKE_GAME WHERE user_name = %s;", (username,))
            level = cur.fetchone()
            if level:
                print(f"Welcome back, {username}! Your current level is {level[0]}")
                self.snake = Snake(INITIAL_FPS)
                self.snake.level = level[0]
            else:
                print(f"Welcome, {username}!")
        except psycopg2.Error as e:
            print("Error loading user data:", e)

    def draw_food(self):
        food_rect = pygame.Rect(self.snake.food_position[0], self.snake.food_position[1], GRID_SIZE, GRID_SIZE)
        food_image = self.food_images[self.snake.food_weight]
        self.screen.blit(food_image, food_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((1, 0))

            self.screen.fill(WHITE)
            if time.time() >= self.snake.food_timer:
                self.snake.food_position = self.snake.generate_food_position()
                self.snake.food_weight = self.snake.generate_food_weight()
                self.snake.food_timer = time.time() + FOOD_TIMER  # когда следует сгенерировать новую еду в игре

            game_over = self.snake.move()
            if game_over:
                running = False
                self.game_over()
            self.draw_snake()
            self.draw_food()
            self.draw_score_and_level()
            pygame.display.flip()
            self.clock.tick(self.snake.fps)  # Устанавливаем FPS в соответствии со скоростью змеи
        pygame.quit()

    def draw_snake(self):
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    def draw_score_and_level(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.snake.score}", True, BLACK)
        level_text = font.render(f"Level: {self.snake.level}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 40))

    def game_over(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, BLACK)
        score_text = font.render(f"Score: {self.snake.score}", True, BLACK)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()

        # Save score to database
        self.save_score_to_db()

    def save_score_to_db(self):
        try:
            cur = self.db_conn.cursor()
            cur.execute("INSERT INTO SNAKE_GAME (user_name, user_score, level) VALUES (%s, %s, %s);", ('Player', self.snake.score, self.snake.level))
            self.db_conn.commit()
            print("Score saved to database successfully")
        except psycopg2.Error as e:
            print("Error saving score to database:", e)
        finally:
            self.db_conn.close()

if __name__ == "__main__":
    game = Game()
    game.start()
