import pygame
import random
from enum import Enum

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GAME_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Direction Enum
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        self.reset_game()
        
    def reset_game(self):
        """Initialize game state"""
        # Snake starts in the middle
        self.snake = [(SCREEN_WIDTH // 2 // GRID_SIZE, SCREEN_HEIGHT // 2 // GRID_SIZE)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        
    def spawn_food(self):
        """Generate random food position"""
        while True:
            x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1)
            y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def handle_events(self):
        """Handle user input and window events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.next_direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.next_direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.next_direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.next_direction = Direction.RIGHT
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
        
        return True
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH // GRID_SIZE or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT // GRID_SIZE):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw(self):
        """Draw game objects"""
        self.screen.fill(BLACK)
        
        # Draw snake
        for segment in self.snake:
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE
            pygame.draw.rect(self.screen, GREEN, (x, y, GRID_SIZE - 2, GRID_SIZE - 2))
        
        # Draw food
        food_x = self.food[0] * GRID_SIZE
        food_y = self.food[1] * GRID_SIZE
        pygame.draw.rect(self.screen, RED, (food_x, food_y, GRID_SIZE - 2, GRID_SIZE - 2))
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press R to Restart", True, YELLOW)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(GAME_SPEED)
        
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
