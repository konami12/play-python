"""
Tests para JME-11: Feature - Victoria del Usuario en Ronda

Este archivo contiene tests exhaustivos para validar la lógica de victoria
del usuario en cada ronda del juego.
"""

import pytest
from src.game_enums import GameChoice, GameResult
from src.game import RockPaperScissorsGame


class TestJME11VictoriaUsuario:
    """Test suite para validar la victoria del usuario en ronda (JME-11)."""

    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame()

    # Tests para todas las combinaciones ganadoras del usuario
    def test_piedra_vs_tijeras_usuario_gana(self):
        """Test: Usuario con Piedra vence Tijeras de computadora."""
        # Given
        user_choice = GameChoice.ROCK
        computer_choice = GameChoice.SCISSORS
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Piedra aplasta Tijeras"

    def test_piedra_vs_lagarto_usuario_gana(self):
        """Test: Usuario con Piedra vence Lagarto de computadora."""
        # Given
        user_choice = GameChoice.ROCK
        computer_choice = GameChoice.LIZARD
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Piedra aplasta Lagarto"

    def test_papel_vs_piedra_usuario_gana(self):
        """Test: Usuario con Papel vence Piedra de computadora."""
        # Given
        user_choice = GameChoice.PAPER
        computer_choice = GameChoice.ROCK
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Papel cubre Piedra"

    def test_papel_vs_spock_usuario_gana(self):
        """Test: Usuario con Papel vence Spock de computadora."""
        # Given
        user_choice = GameChoice.PAPER
        computer_choice = GameChoice.SPOCK
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Papel desautoriza Spock"

    def test_tijeras_vs_papel_usuario_gana(self):
        """Test: Usuario con Tijeras vence Papel de computadora."""
        # Given
        user_choice = GameChoice.SCISSORS
        computer_choice = GameChoice.PAPER
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Tijeras cortan Papel"

    def test_tijeras_vs_lagarto_usuario_gana(self):
        """Test: Usuario con Tijeras vence Lagarto de computadora."""
        # Given
        user_choice = GameChoice.SCISSORS
        computer_choice = GameChoice.LIZARD
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Tijeras decapitan Lagarto"

    def test_lagarto_vs_papel_usuario_gana(self):
        """Test: Usuario con Lagarto vence Papel de computadora."""
        # Given
        user_choice = GameChoice.LIZARD
        computer_choice = GameChoice.PAPER
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Lagarto come Papel"

    def test_lagarto_vs_spock_usuario_gana(self):
        """Test: Usuario con Lagarto vence Spock de computadora."""
        # Given
        user_choice = GameChoice.LIZARD
        computer_choice = GameChoice.SPOCK
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Lagarto envenena Spock"

    def test_spock_vs_tijeras_usuario_gana(self):
        """Test: Usuario con Spock vence Tijeras de computadora."""
        # Given
        user_choice = GameChoice.SPOCK
        computer_choice = GameChoice.SCISSORS
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Spock aplasta Tijeras"

    def test_spock_vs_piedra_usuario_gana(self):
        """Test: Usuario con Spock vence Piedra de computadora."""
        # Given
        user_choice = GameChoice.SPOCK
        computer_choice = GameChoice.ROCK
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.USER_WINS
        assert user_choice.beats(computer_choice) is True
        assert user_choice.get_win_description(computer_choice) == "Spock vaporiza Piedra"

    # Tests de actualización del marcador
    def test_marcador_aumenta_cuando_usuario_gana(self):
        """Test: El marcador del usuario aumenta en 1 cuando gana."""
        # Given
        marcador_inicial = self.game.user_score
        result = GameResult.USER_WINS
        
        # When
        self.game._update_score(result)
        
        # Then
        assert self.game.user_score == marcador_inicial + 1
        assert self.game.computer_score == 0  # No debe cambiar

    def test_marcador_no_cambia_cuando_computadora_gana(self):
        """Test: El marcador del usuario no cambia cuando pierde."""
        # Given
        marcador_inicial = self.game.user_score
        result = GameResult.COMPUTER_WINS
        
        # When
        self.game._update_score(result)
        
        # Then
        assert self.game.user_score == marcador_inicial  # No debe cambiar
        assert self.game.computer_score == 1

    def test_marcador_no_cambia_en_empate(self):
        """Test: El marcador no cambia en caso de empate."""
        # Given
        marcador_usuario_inicial = self.game.user_score
        marcador_computadora_inicial = self.game.computer_score
        result = GameResult.TIE
        
        # When
        self.game._update_score(result)
        
        # Then
        assert self.game.user_score == marcador_usuario_inicial
        assert self.game.computer_score == marcador_computadora_inicial

    # Tests de combinaciones perdedoras (para completitud)
    def test_usuario_pierde_combinaciones_correctas(self):
        """Test: Usuario pierde cuando debería perder."""
        combinaciones_perdedoras = [
            (GameChoice.ROCK, GameChoice.PAPER),      # Papel cubre Piedra
            (GameChoice.ROCK, GameChoice.SPOCK),      # Spock vaporiza Piedra
            (GameChoice.PAPER, GameChoice.SCISSORS),  # Tijeras cortan Papel
            (GameChoice.PAPER, GameChoice.LIZARD),    # Lagarto come Papel
            (GameChoice.SCISSORS, GameChoice.ROCK),   # Piedra aplasta Tijeras
            (GameChoice.SCISSORS, GameChoice.SPOCK),  # Spock aplasta Tijeras
            (GameChoice.LIZARD, GameChoice.ROCK),     # Piedra aplasta Lagarto
            (GameChoice.LIZARD, GameChoice.SCISSORS), # Tijeras decapitan Lagarto
            (GameChoice.SPOCK, GameChoice.PAPER),     # Papel desautoriza Spock
            (GameChoice.SPOCK, GameChoice.LIZARD),    # Lagarto envenena Spock
        ]
        
        for user_choice, computer_choice in combinaciones_perdedoras:
            result = self.game.compare_choices(user_choice, computer_choice)
            assert result == GameResult.COMPUTER_WINS, \
                f"Usuario con {user_choice} debería perder contra {computer_choice}"

    # Tests de escenario específico del ticket
    def test_scenario_piedra_vs_tijeras_incrementa_marcador(self):
        """Test: Escenario específico del ticket - Piedra vs Tijeras."""
        # Given el usuario selecciona "Piedra"
        user_choice = GameChoice.ROCK
        # And la computadora selecciona "Tijeras"
        computer_choice = GameChoice.SCISSORS
        marcador_inicial = self.game.user_score
        
        # When se comparan las elecciones
        result = self.game.compare_choices(user_choice, computer_choice)
        self.game._update_score(result)
        
        # Then el usuario debe ganar la ronda
        assert result == GameResult.USER_WINS
        # And el marcador del usuario debe aumentar en 1
        assert self.game.user_score == marcador_inicial + 1

    # Tests de reglas completas del juego
    def test_reglas_completas_implementadas(self):
        """Test: Todas las reglas del juego están correctamente implementadas."""
        reglas_esperadas = {
            # Piedra aplasta Tijeras y Lagarto
            GameChoice.ROCK: [GameChoice.SCISSORS, GameChoice.LIZARD],
            # Papel cubre Piedra y desautoriza Spock
            GameChoice.PAPER: [GameChoice.ROCK, GameChoice.SPOCK],
            # Tijeras cortan Papel y decapitan Lagarto
            GameChoice.SCISSORS: [GameChoice.PAPER, GameChoice.LIZARD],
            # Lagarto come Papel y envenena Spock
            GameChoice.LIZARD: [GameChoice.PAPER, GameChoice.SPOCK],
            # Spock aplasta Tijeras y vaporiza Piedra
            GameChoice.SPOCK: [GameChoice.SCISSORS, GameChoice.ROCK]
        }
        
        for atacante, victimas in reglas_esperadas.items():
            for victima in victimas:
                assert atacante.beats(victima), \
                    f"{atacante} debería vencer a {victima}"
                # También verificar que la descripción existe
                descripcion = atacante.get_win_description(victima)
                assert descripcion != f"{atacante} vence a {victima}", \
                    f"Falta descripción específica para {atacante} vs {victima}"

    # Tests de mensajes de victoria
    def test_mensajes_victoria_son_descriptivos(self):
        """Test: Los mensajes de victoria son descriptivos y específicos."""
        combinaciones_ganadoras = [
            (GameChoice.ROCK, GameChoice.SCISSORS, "Piedra aplasta Tijeras"),
            (GameChoice.ROCK, GameChoice.LIZARD, "Piedra aplasta Lagarto"),
            (GameChoice.PAPER, GameChoice.ROCK, "Papel cubre Piedra"),
            (GameChoice.PAPER, GameChoice.SPOCK, "Papel desautoriza Spock"),
            (GameChoice.SCISSORS, GameChoice.PAPER, "Tijeras cortan Papel"),
            (GameChoice.SCISSORS, GameChoice.LIZARD, "Tijeras decapitan Lagarto"),
            (GameChoice.LIZARD, GameChoice.PAPER, "Lagarto come Papel"),
            (GameChoice.LIZARD, GameChoice.SPOCK, "Lagarto envenena Spock"),
            (GameChoice.SPOCK, GameChoice.SCISSORS, "Spock aplasta Tijeras"),
            (GameChoice.SPOCK, GameChoice.ROCK, "Spock vaporiza Piedra"),
        ]
        
        for ganador, perdedor, mensaje_esperado in combinaciones_ganadoras:
            mensaje_actual = ganador.get_win_description(perdedor)
            assert mensaje_actual == mensaje_esperado, \
                f"Mensaje incorrecto para {ganador} vs {perdedor}. " \
                f"Esperado: '{mensaje_esperado}', Actual: '{mensaje_actual}'"

    # Test de integración
    def test_flujo_completo_victoria_usuario(self):
        """Test: Flujo completo cuando usuario gana una ronda."""
        # Given
        initial_user_score = self.game.user_score
        initial_computer_score = self.game.computer_score
        user_choice = GameChoice.ROCK
        computer_choice = GameChoice.SCISSORS
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        self.game._update_score(result)
        
        # Then
        assert result == GameResult.USER_WINS
        assert self.game.user_score == initial_user_score + 1
        assert self.game.computer_score == initial_computer_score
        assert user_choice.beats(computer_choice) is True
        
        # And verificar descripción
        description = user_choice.get_win_description(computer_choice)
        assert "Piedra aplasta Tijeras" == description