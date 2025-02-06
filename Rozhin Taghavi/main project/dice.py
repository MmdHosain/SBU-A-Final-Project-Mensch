import random
import pygame

def roll_dice():
    """Rolls a dice and returns a random number between 1 and 6."""
    return random.randint(1, 6)



def draw_dice(screen, player_dice_roll, current_player, player_colors, screen_size):
    """Displays the dice roll result and current player's turn on the screen."""

    print(f"{current_player + 1} roll dice:{player_dice_roll}")
    font = pygame.font.Font(None, 40)

    # Show dice number
    dice_text = font.render(f"Dice: {player_dice_roll}", True, (0, 0, 0))
    screen.blit(dice_text, (screen_size - 170, 20))  # Top-right corner

    # Show current player's turn
    turn_text = font.render(f"Turn: Player {current_player + 1}", True, player_colors[current_player])
    screen.blit(turn_text, (20, 20))  # Top-left corner
import random



