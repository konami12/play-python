"""
Enumeraciones para el juego Piedra, Papel, Tijeras, Lagarto, Spock

Este módulo contiene las definiciones de Enum para las opciones del juego
y otros estados necesarios.
"""

from enum import Enum
from typing import Dict, List


class GameChoice(Enum):
    """Enum para las opciones del juego Piedra, Papel, Tijeras, Lagarto, Spock."""
    
    ROCK = "Piedra"
    PAPER = "Papel"
    SCISSORS = "Tijeras"
    LIZARD = "Lagarto"
    SPOCK = "Spock"
    
    def __str__(self) -> str:
        return self.value
    
    @classmethod
    def get_choices_dict(cls) -> Dict[int, 'GameChoice']:
        """
        Retorna un diccionario que mapea números (1-5) a opciones del juego.
        
        Returns:
            Dict[int, GameChoice]: Diccionario con mapeo numérico
        """
        return {
            1: cls.ROCK,
            2: cls.PAPER,
            3: cls.SCISSORS,
            4: cls.LIZARD,
            5: cls.SPOCK
        }
    
    @classmethod
    def get_choice_by_number(cls, number: int) -> 'GameChoice':
        """
        Obtiene una opción del juego por su número.
        
        Args:
            number: Número del 1 al 5
            
        Returns:
            GameChoice: La opción correspondiente
            
        Raises:
            ValueError: Si el número no está en el rango 1-5
        """
        choices = cls.get_choices_dict()
        if number not in choices:
            raise ValueError(f"Número inválido: {number}. Debe ser entre 1 y 5.")
        return choices[number]
    
    @classmethod
    def get_all_choices(cls) -> List['GameChoice']:
        """
        Retorna todas las opciones del juego como lista.
        
        Returns:
            List[GameChoice]: Lista con todas las opciones
        """
        return list(cls)
    
    def beats(self, other: 'GameChoice') -> bool:
        """
        Determina si esta opción vence a otra.
        
        Args:
            other: La otra opción del juego
            
        Returns:
            bool: True si esta opción vence a la otra
        """
        winning_combinations = {
            GameChoice.ROCK: [GameChoice.SCISSORS, GameChoice.LIZARD],
            GameChoice.PAPER: [GameChoice.ROCK, GameChoice.SPOCK],
            GameChoice.SCISSORS: [GameChoice.PAPER, GameChoice.LIZARD],
            GameChoice.LIZARD: [GameChoice.PAPER, GameChoice.SPOCK],
            GameChoice.SPOCK: [GameChoice.SCISSORS, GameChoice.ROCK]
        }
        
        return other in winning_combinations.get(self, [])
    
    def get_win_description(self, other: 'GameChoice') -> str:
        """
        Obtiene la descripción de cómo esta opción vence a otra.
        
        Args:
            other: La opción que es vencida
            
        Returns:
            str: Descripción de la victoria
        """
        descriptions = {
            (GameChoice.ROCK, GameChoice.SCISSORS): "Piedra aplasta Tijeras",
            (GameChoice.ROCK, GameChoice.LIZARD): "Piedra aplasta Lagarto",
            (GameChoice.PAPER, GameChoice.ROCK): "Papel cubre Piedra",
            (GameChoice.PAPER, GameChoice.SPOCK): "Papel desautoriza Spock",
            (GameChoice.SCISSORS, GameChoice.PAPER): "Tijeras cortan Papel",
            (GameChoice.SCISSORS, GameChoice.LIZARD): "Tijeras decapitan Lagarto",
            (GameChoice.LIZARD, GameChoice.PAPER): "Lagarto come Papel",
            (GameChoice.LIZARD, GameChoice.SPOCK): "Lagarto envenena Spock",
            (GameChoice.SPOCK, GameChoice.SCISSORS): "Spock aplasta Tijeras",
            (GameChoice.SPOCK, GameChoice.ROCK): "Spock vaporiza Piedra"
        }
        
        return descriptions.get((self, other), f"{self} vence a {other}")


class GameResult(Enum):
    """Enum para los resultados de una ronda."""
    
    USER_WINS = "user_wins"
    COMPUTER_WINS = "computer_wins"
    TIE = "tie"
    
    def __str__(self) -> str:
        result_strings = {
            GameResult.USER_WINS: "¡Ganaste!",
            GameResult.COMPUTER_WINS: "Ganó la computadora",
            GameResult.TIE: "¡Empate!"
        }
        return result_strings[self]


class GameState(Enum):
    """Enum para los estados del juego."""
    
    MENU = "menu"
    PLAYING = "playing"
    GAME_OVER = "game_over"
    QUIT = "quit"