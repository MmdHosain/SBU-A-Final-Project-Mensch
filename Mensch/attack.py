import movement
import pygame


import movement
import pygame

def attack(board, attacking_piece):
    for color, pieces in board.items():
        if color != attacking_piece['color']:
            for piece_name, piece_info in pieces.items():
                if isinstance(piece_info, dict) and piece_info.get('position') is not None and piece_info['position'] == attacking_piece['position']:
                    piece_info['position'] = movement.get_base_position(piece_info['color'], board)
                    print(f"{piece_info['color']} piece at {piece_info['position']} has been attacked and moved to base.")