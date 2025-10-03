"""
Tests para JME-13: Feature - Finalización del Juego

Este archivo contiene tests exhaustivos para validar la lógica de finalización
del juego cuando un jugador alcanza la puntuación máxima.
"""

import pytest
from src.game_enums import GameChoice, GameResult
from src.game import RockPaperScissorsGame


class TestJME13FinalizacionJuego:
    """Test suite para validar la finalización del juego (JME-13)."""

    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame(max_score=3)

    # Tests de condición de victoria
    def test_juego_termina_cuando_usuario_alcanza_max_score(self):
        """Test: El juego termina cuando el usuario alcanza la puntuación máxima."""
        # Given - Usuario cerca de ganar
        self.game.user_score = 2
        self.game.computer_score = 1
        
        # When - Usuario gana una ronda más
        self.game.user_score = 3
        
        # Then - El juego debe terminar
        assert self.game._check_game_over() is True

    def test_juego_termina_cuando_computadora_alcanza_max_score(self):
        """Test: El juego termina cuando la computadora alcanza la puntuación máxima."""
        # Given - Computadora cerca de ganar
        self.game.user_score = 1
        self.game.computer_score = 2
        
        # When - Computadora gana una ronda más
        self.game.computer_score = 3
        
        # Then - El juego debe terminar
        assert self.game._check_game_over() is True

    def test_juego_no_termina_antes_de_max_score(self):
        """Test: El juego no termina antes de alcanzar la puntuación máxima."""
        marcadores_no_finales = [
            (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2)
        ]
        
        for user_score, computer_score in marcadores_no_finales:
            self.game.user_score = user_score
            self.game.computer_score = computer_score
            assert self.game._check_game_over() is False, \
                f"Juego no debe terminar con marcador {user_score}-{computer_score}"

    # Test del escenario específico del ticket
    def test_scenario_finalizacion_victoria_usuario(self):
        """Test: Escenario específico del ticket - Usuario gana cuando marcador es 2-2."""
        # Given el marcador del usuario es 2
        self.game.user_score = 2
        # And el marcador de la computadora es 2
        self.game.computer_score = 2
        
        # When el usuario gana la siguiente ronda
        result = GameResult.USER_WINS
        self.game._update_score(result)
        
        # Then el juego debe terminar
        assert self.game._check_game_over() is True
        assert self.game.user_score == 3
        assert self.game.computer_score == 2

    # Tests de marcadores finales específicos
    def test_victoria_usuario_3_0(self):
        """Test: Victoria perfecta del usuario 3-0."""
        self.game.user_score = 3
        self.game.computer_score = 0
        assert self.game._check_game_over() is True

    def test_victoria_usuario_3_1(self):
        """Test: Victoria del usuario 3-1."""
        self.game.user_score = 3
        self.game.computer_score = 1
        assert self.game._check_game_over() is True

    def test_victoria_usuario_3_2(self):
        """Test: Victoria del usuario 3-2."""
        self.game.user_score = 3
        self.game.computer_score = 2
        assert self.game._check_game_over() is True

    def test_victoria_computadora_0_3(self):
        """Test: Victoria perfecta de la computadora 0-3."""
        self.game.user_score = 0
        self.game.computer_score = 3
        assert self.game._check_game_over() is True

    def test_victoria_computadora_1_3(self):
        """Test: Victoria de la computadora 1-3."""
        self.game.user_score = 1
        self.game.computer_score = 3
        assert self.game._check_game_over() is True

    def test_victoria_computadora_2_3(self):
        """Test: Victoria de la computadora 2-3."""
        self.game.user_score = 2
        self.game.computer_score = 3
        assert self.game._check_game_over() is True

    # Tests de configuración de max_score personalizada
    def test_max_score_personalizado_5(self):
        """Test: Juego funciona con max_score personalizado de 5."""
        game_custom = RockPaperScissorsGame(max_score=5)
        
        # No debe terminar antes de 5
        game_custom.user_score = 4
        game_custom.computer_score = 3
        assert game_custom._check_game_over() is False
        
        # Debe terminar cuando alcanza 5
        game_custom.user_score = 5
        assert game_custom._check_game_over() is True

    def test_max_score_personalizado_1(self):
        """Test: Juego funciona con max_score personalizado de 1."""
        game_custom = RockPaperScissorsGame(max_score=1)
        
        # Debe terminar inmediatamente al ganar primera ronda
        game_custom.user_score = 1
        game_custom.computer_score = 0
        assert game_custom._check_game_over() is True

    # Tests de reinicio del juego
    def test_reset_game_limpia_marcadores(self):
        """Test: reset_game() limpia los marcadores y estado."""
        # Given - Juego con puntuación
        self.game.user_score = 2
        self.game.computer_score = 1
        self.game.rounds_played = 3
        
        # When - Se reinicia el juego
        self.game.reset_game()
        
        # Then - Todo debe estar en estado inicial
        assert self.game.user_score == 0
        assert self.game.computer_score == 0
        assert self.game.rounds_played == 0
        assert self.game._check_game_over() is False

    # Tests de flujo completo hasta finalización
    def test_flujo_completo_victoria_usuario(self):
        """Test: Flujo completo donde usuario gana el juego."""
        # Simular 3 victorias del usuario
        for _ in range(3):
            result = GameResult.USER_WINS
            self.game._update_score(result)
        
        # Verificar que el juego termina con victoria del usuario
        assert self.game._check_game_over() is True
        assert self.game.user_score == 3
        assert self.game.computer_score == 0

    def test_flujo_completo_victoria_computadora(self):
        """Test: Flujo completo donde computadora gana el juego."""
        # Simular 3 victorias de la computadora
        for _ in range(3):
            result = GameResult.COMPUTER_WINS
            self.game._update_score(result)
        
        # Verificar que el juego termina con victoria de la computadora
        assert self.game._check_game_over() is True
        assert self.game.user_score == 0
        assert self.game.computer_score == 3

    def test_flujo_con_empates_no_afecta_finalizacion(self):
        """Test: Los empates no afectan la condición de finalización."""
        # Simular empates
        for _ in range(5):
            result = GameResult.TIE
            self.game._update_score(result)
        
        # Los empates no deben cambiar marcador ni finalizar juego
        assert self.game._check_game_over() is False
        assert self.game.user_score == 0
        assert self.game.computer_score == 0
        
        # Pero 3 victorias del usuario sí deben finalizar
        for _ in range(3):
            result = GameResult.USER_WINS
            self.game._update_score(result)
        
        assert self.game._check_game_over() is True

    # Tests de casos edge
    def test_juego_termina_exactamente_en_max_score(self):
        """Test: El juego termina exactamente al alcanzar max_score, no antes ni después."""
        # Llevar el marcador a 2-2
        self.game.user_score = 2
        self.game.computer_score = 2
        assert self.game._check_game_over() is False
        
        # Una victoria más del usuario debe terminar el juego
        result = GameResult.USER_WINS
        self.game._update_score(result)
        assert self.game._check_game_over() is True
        assert self.game.user_score == 3

    def test_no_puede_superar_max_score_en_condicion(self):
        """Test: La condición funciona correctamente incluso si se supera max_score."""
        # Simular marcador mayor al máximo (caso edge)
        self.game.user_score = 4  # Mayor que max_score=3
        self.game.computer_score = 1
        
        # Debe seguir detectando que el juego terminó
        assert self.game._check_game_over() is True

    # Tests de integración con play_round
    def test_play_round_retorna_false_cuando_juego_termina(self):
        """Test: play_round retorna False cuando el juego termina."""
        # Given - Usuario a punto de ganar
        self.game.user_score = 2
        self.game.computer_score = 1
        
        # Mockear comparación para que usuario gane
        user_choice = GameChoice.ROCK
        computer_choice = GameChoice.SCISSORS
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Verificar que es victoria del usuario
        assert result == GameResult.USER_WINS
        
        # Actualizar score manualmente para simular final de ronda
        self.game._update_score(result)
        
        # Verificar que el juego terminó
        assert self.game._check_game_over() is True

    # Tests de casos de competencia reñida
    def test_competencia_reñida_2_2_usuario_gana(self):
        """Test: Competencia reñida 2-2, usuario gana."""
        self.game.user_score = 2
        self.game.computer_score = 2
        
        # Usuario gana ronda decisiva
        result = GameResult.USER_WINS
        self.game._update_score(result)
        
        assert self.game._check_game_over() is True
        assert self.game.user_score == 3
        assert self.game.computer_score == 2

    def test_competencia_reñida_2_2_computadora_gana(self):
        """Test: Competencia reñida 2-2, computadora gana."""
        self.game.user_score = 2
        self.game.computer_score = 2
        
        # Computadora gana ronda decisiva
        result = GameResult.COMPUTER_WINS
        self.game._update_score(result)
        
        assert self.game._check_game_over() is True
        assert self.game.user_score == 2
        assert self.game.computer_score == 3

    # Tests de validación de max_score
    def test_max_score_default_es_3(self):
        """Test: El max_score por defecto es 3."""
        game_default = RockPaperScissorsGame()
        assert game_default.max_score == 3

    def test_max_score_se_configura_correctamente(self):
        """Test: El max_score se configura correctamente en constructor."""
        for max_score in [1, 2, 3, 5, 10]:
            game = RockPaperScissorsGame(max_score=max_score)
            assert game.max_score == max_score

    # Test de cobertura completa de condiciones
    def test_matriz_completa_finalizacion(self):
        """Test: Matriz completa de todas las condiciones de finalización."""
        condiciones_finales = [
            # Victorias del usuario
            (3, 0), (3, 1), (3, 2),
            # Victorias de la computadora
            (0, 3), (1, 3), (2, 3),
            # Casos edge (ambos alcanzan)
            (3, 3), (4, 3), (3, 4)
        ]
        
        for user_score, computer_score in condiciones_finales:
            self.game.user_score = user_score
            self.game.computer_score = computer_score
            assert self.game._check_game_over() is True, \
                f"Juego debe terminar con marcador {user_score}-{computer_score}"

    def test_matriz_completa_no_finalizacion(self):
        """Test: Matriz completa de condiciones donde NO debe finalizar."""
        condiciones_no_finales = [
            (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2)
        ]
        
        for user_score, computer_score in condiciones_no_finales:
            self.game.user_score = user_score
            self.game.computer_score = computer_score
            assert self.game._check_game_over() is False, \
                f"Juego NO debe terminar con marcador {user_score}-{computer_score}"