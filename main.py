import pygame
from game import SnakeGameAI

          

if __name__ == '__main__':
    game = SnakeGameAI()
    
    # game loop
    while True:
        game_over, score = game.play_step()
        
        if game_over == True:
            break
        
    print('Final Score', score)
    pygame.quit()