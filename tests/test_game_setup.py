"""
Tests básicos para el setup del juego Piedra, Papel, Tijeras, Lagarto, Spock

Estos tests validan que el stack tecnológico esté correctamente configurado.
"""

import pytest
from src.game_enums import GameChoice, GameResult, GameState
from src.game import RockPaperScissorsGame


class TestGameSetup:
    """Tests para validar la configuración inicial del juego."""
    
    def test_python_version(self):
        """Test: Verificar que estamos usando Python 3.12+"""
        import sys
        major, minor = sys.version_info[:2]
        assert major == 3
        assert minor >= 12, f"Se requiere Python 3.12+, se encontró {major}.{minor}"
    
    def test_colorama_import(self):
        """Test: Verificar que colorama esté disponible"""
        try:
            import colorama
            assert hasattr(colorama, 'Fore')
            assert hasattr(colorama, 'Back')
            assert hasattr(colorama, 'Style')
        except ImportError:
            pytest.fail("colorama no está instalado o no se puede importar")


class TestGameEnums:
    """Tests para validar los Enums del juego."""
    
    def test_game_choice_enum_values(self):
        """Test: Verificar que GameChoice tiene todas las opciones correctas"""
        expected_choices = {"Piedra", "Papel", "Tijeras", "Lagarto", "Spock"}
        actual_choices = {choice.value for choice in GameChoice}
        assert actual_choices == expected_choices
    
    def test_game_choice_numbers_mapping(self):
        """Test: Verificar mapeo correcto de números a opciones"""
        choices_dict = GameChoice.get_choices_dict()
        
        assert len(choices_dict) == 5
        assert all(1 <= key <= 5 for key in choices_dict.keys())
        assert GameChoice.ROCK in choices_dict.values()
        assert GameChoice.PAPER in choices_dict.values()
        assert GameChoice.SCISSORS in choices_dict.values()
        assert GameChoice.LIZARD in choices_dict.values()
        assert GameChoice.SPOCK in choices_dict.values()
    
    def test_game_choice_by_number(self):
        """Test: Verificar obtención de opciones por número"""
        assert GameChoice.get_choice_by_number(1) == GameChoice.ROCK
        assert GameChoice.get_choice_by_number(2) == GameChoice.PAPER
        assert GameChoice.get_choice_by_number(3) == GameChoice.SCISSORS
        assert GameChoice.get_choice_by_number(4) == GameChoice.LIZARD
        assert GameChoice.get_choice_by_number(5) == GameChoice.SPOCK
    
    def test_invalid_choice_number(self):
        """Test: Verificar que números inválidos lancen error"""
        with pytest.raises(ValueError):
            GameChoice.get_choice_by_number(0)
        
        with pytest.raises(ValueError):
            GameChoice.get_choice_by_number(6)
        
        with pytest.raises(ValueError):
            GameChoice.get_choice_by_number(-1)
    
    def test_game_result_enum(self):
        """Test: Verificar que GameResult tiene todos los valores"""
        assert GameResult.USER_WINS.value == "user_wins"
        assert GameResult.COMPUTER_WINS.value == "computer_wins"
        assert GameResult.TIE.value == "tie"
    
    def test_game_state_enum(self):
        """Test: Verificar que GameState tiene todos los estados"""
        assert GameState.MENU.value == "menu"
        assert GameState.PLAYING.value == "playing"
        assert GameState.GAME_OVER.value == "game_over"
        assert GameState.QUIT.value == "quit"


class TestGameLogic:
    """Tests básicos para la lógica del juego."""
    
    def test_game_initialization(self):
        """Test: Verificar inicialización correcta del juego"""
        game = RockPaperScissorsGame()
        
        assert game.max_score == 3  # Default
        assert game.user_score == 0
        assert game.computer_score == 0
        assert game.state == GameState.MENU
        assert game.rounds_played == 0
    
    def test_game_initialization_custom_score(self):
        """Test: Verificar inicialización con puntuación personalizada"""
        game = RockPaperScissorsGame(max_score=5)
        assert game.max_score == 5
    
    def test_game_reset(self):
        """Test: Verificar reset del juego"""
        game = RockPaperScissorsGame()
        
        # Simular estado modificado
        game.user_score = 2
        game.computer_score = 1
        game.rounds_played = 3
        game.state = GameState.PLAYING
        
        # Reset
        game.reset_game()
        
        # Verificar que volvió al estado inicial
        assert game.user_score == 0
        assert game.computer_score == 0
        assert game.rounds_played == 0
        assert game.state == GameState.MENU
    
    def test_computer_choice_generation(self):
        """Test: Verificar que la computadora puede generar elecciones válidas"""
        game = RockPaperScissorsGame()
        
        # Generar múltiples elecciones para asegurar aleatoriedad
        choices = [game.get_computer_choice() for _ in range(10)]
        
        # Todas las elecciones deben ser válidas
        valid_choices = set(GameChoice)
        for choice in choices:
            assert choice in valid_choices
    
    def test_choice_comparison_tie(self):
        """Test: Verificar detección de empates"""
        game = RockPaperScissorsGame()
        
        for choice in GameChoice:
            result = game.compare_choices(choice, choice)
            assert result == GameResult.TIE


class TestGameRules:
    """Tests para validar las reglas específicas del juego."""
    
    @pytest.mark.parametrize("winner,loser", [
        (GameChoice.ROCK, GameChoice.SCISSORS),
        (GameChoice.ROCK, GameChoice.LIZARD),
        (GameChoice.PAPER, GameChoice.ROCK),
        (GameChoice.PAPER, GameChoice.SPOCK),
        (GameChoice.SCISSORS, GameChoice.PAPER),
        (GameChoice.SCISSORS, GameChoice.LIZARD),
        (GameChoice.LIZARD, GameChoice.PAPER),
        (GameChoice.LIZARD, GameChoice.SPOCK),
        (GameChoice.SPOCK, GameChoice.SCISSORS),
        (GameChoice.SPOCK, GameChoice.ROCK),
    ])
    def test_winning_combinations(self, winner, loser):
        """Test: Verificar todas las combinaciones ganadoras"""
        assert winner.beats(loser), f"{winner} debería vencer a {loser}"
        
        game = RockPaperScissorsGame()
        result = game.compare_choices(winner, loser)
        assert result == GameResult.USER_WINS
    
    def test_win_descriptions(self):
        """Test: Verificar que todas las combinaciones ganadoras tienen descripción"""
        winning_combinations = [
            (GameChoice.ROCK, GameChoice.SCISSORS),
            (GameChoice.ROCK, GameChoice.LIZARD),
            (GameChoice.PAPER, GameChoice.ROCK),
            (GameChoice.PAPER, GameChoice.SPOCK),
            (GameChoice.SCISSORS, GameChoice.PAPER),
            (GameChoice.SCISSORS, GameChoice.LIZARD),
            (GameChoice.LIZARD, GameChoice.PAPER),
            (GameChoice.LIZARD, GameChoice.SPOCK),
            (GameChoice.SPOCK, GameChoice.SCISSORS),
            (GameChoice.SPOCK, GameChoice.ROCK),
        ]
        
        for winner, loser in winning_combinations:
            description = winner.get_win_description(loser)
            assert isinstance(description, str)
            assert len(description) > 0
            assert winner.value in description or loser.value in description