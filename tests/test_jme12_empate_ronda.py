"""
Tests para JME-12: Feature - Manejo de Empates

Este archivo contiene tests exhaustivos para validar la lógica de empates
cuando ambos jugadores eligen la misma opción.
"""

import pytest
from src.game_enums import GameChoice, GameResult, GameState
from src.game import RockPaperScissorsGame


class TestJME12ManejoEmpates:
    """Test suite para validar el manejo de empates en ronda (JME-12)."""

    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame()

    # Tests para todos los empates posibles
    def test_empate_piedra_vs_piedra(self):
        """Test: Empate cuando ambos eligen Piedra."""
        # Given
        user_choice = GameChoice.ROCK
        computer_choice = GameChoice.ROCK
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.TIE
        assert user_choice == computer_choice

    def test_empate_papel_vs_papel(self):
        """Test: Empate cuando ambos eligen Papel."""
        # Given
        user_choice = GameChoice.PAPER
        computer_choice = GameChoice.PAPER
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.TIE
        assert user_choice == computer_choice

    def test_empate_tijeras_vs_tijeras(self):
        """Test: Empate cuando ambos eligen Tijeras."""
        # Given
        user_choice = GameChoice.SCISSORS
        computer_choice = GameChoice.SCISSORS
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.TIE
        assert user_choice == computer_choice

    def test_empate_lagarto_vs_lagarto(self):
        """Test: Empate cuando ambos eligen Lagarto."""
        # Given
        user_choice = GameChoice.LIZARD
        computer_choice = GameChoice.LIZARD
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.TIE
        assert user_choice == computer_choice

    def test_empate_spock_vs_spock(self):
        """Test: Empate cuando ambos eligen Spock."""
        # Given
        user_choice = GameChoice.SPOCK
        computer_choice = GameChoice.SPOCK
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        
        # Then
        assert result == GameResult.TIE
        assert user_choice == computer_choice

    # Tests de marcador en empates
    def test_marcador_no_cambia_en_empate(self):
        """Test: El marcador no cambia cuando hay empate."""
        # Given
        marcador_usuario_inicial = self.game.user_score
        marcador_computadora_inicial = self.game.computer_score
        result = GameResult.TIE
        
        # When
        self.game._update_score(result)
        
        # Then
        assert self.game.user_score == marcador_usuario_inicial
        assert self.game.computer_score == marcador_computadora_inicial

    def test_multiples_empates_consecutivos(self):
        """Test: Múltiples empates consecutivos no afectan el marcador."""
        # Given
        marcador_usuario_inicial = self.game.user_score
        marcador_computadora_inicial = self.game.computer_score
        
        # When - Simular 5 empates consecutivos
        for _ in range(5):
            result = GameResult.TIE
            self.game._update_score(result)
        
        # Then
        assert self.game.user_score == marcador_usuario_inicial
        assert self.game.computer_score == marcador_computadora_inicial

    # Test del escenario específico del ticket
    def test_scenario_lagarto_vs_lagarto_empate(self):
        """Test: Escenario específico del ticket - Lagarto vs Lagarto."""
        # Given el usuario selecciona "Lagarto"
        user_choice = GameChoice.LIZARD
        # And la computadora selecciona "Lagarto"
        computer_choice = GameChoice.LIZARD
        marcador_usuario_inicial = self.game.user_score
        marcador_computadora_inicial = self.game.computer_score
        
        # When se comparan las elecciones
        result = self.game.compare_choices(user_choice, computer_choice)
        self.game._update_score(result)
        
        # Then debe declararse empate
        assert result == GameResult.TIE
        # And el marcador no debe cambiar
        assert self.game.user_score == marcador_usuario_inicial
        assert self.game.computer_score == marcador_computadora_inicial

    # Tests de lógica de empates
    def test_empate_solo_cuando_elecciones_iguales(self):
        """Test: Solo hay empate cuando las elecciones son exactamente iguales."""
        for choice in GameChoice.get_all_choices():
            # Test empate con la misma elección
            result = self.game.compare_choices(choice, choice)
            assert result == GameResult.TIE
            
            # Test que NO hay empate con elecciones diferentes
            for other_choice in GameChoice.get_all_choices():
                if choice != other_choice:
                    result = self.game.compare_choices(choice, other_choice)
                    assert result != GameResult.TIE

    def test_empate_no_termina_juego(self):
        """Test: Los empates no terminan el juego."""
        # Given un juego con marcador alto pero sin ganar
        self.game.user_score = 2
        self.game.computer_score = 2
        self.game.max_score = 3
        
        # When hay un empate
        result = GameResult.TIE
        self.game._update_score(result)
        
        # Then el juego no debe terminar
        assert not self.game._check_game_over()
        assert self.game.user_score == 2
        assert self.game.computer_score == 2

    # Tests de mensaje de empate
    def test_mensaje_empate_en_gameresult(self):
        """Test: GameResult.TIE tiene el mensaje correcto."""
        result = GameResult.TIE
        assert str(result) == "¡Empate!"

    def test_todas_las_opciones_pueden_empatar(self):
        """Test: Todas las opciones del juego pueden generar empate."""
        opciones = GameChoice.get_all_choices()
        
        for opcion in opciones:
            result = self.game.compare_choices(opcion, opcion)
            assert result == GameResult.TIE, f"{opcion} vs {opcion} debe resultar en empate"

    # Tests de flujo completo con empates
    def test_flujo_completo_empate(self):
        """Test: Flujo completo cuando hay empate."""
        # Given
        initial_user_score = self.game.user_score
        initial_computer_score = self.game.computer_score
        user_choice = GameChoice.ROCK
        computer_choice = GameChoice.ROCK
        
        # When
        result = self.game.compare_choices(user_choice, computer_choice)
        self.game._update_score(result)
        
        # Then
        assert result == GameResult.TIE
        assert self.game.user_score == initial_user_score
        assert self.game.computer_score == initial_computer_score
        assert user_choice == computer_choice

    # Tests de casos edge
    def test_empate_con_diferentes_instancias_misma_opcion(self):
        """Test: Empate funciona con diferentes instancias de la misma opción."""
        choice1 = GameChoice.ROCK
        choice2 = GameChoice.ROCK
        
        # Verificar que son la misma opción pero pueden ser diferentes instancias
        assert choice1 == choice2
        assert choice1 is choice2  # En enums, deberían ser la misma instancia
        
        result = self.game.compare_choices(choice1, choice2)
        assert result == GameResult.TIE

    # Test de regresión para asegurar que empates no rompen otras funcionalidades
    def test_empate_no_afecta_victorias_subsecuentes(self):
        """Test: Un empate no afecta las victorias posteriores."""
        # Given un empate inicial
        tie_result = self.game.compare_choices(GameChoice.ROCK, GameChoice.ROCK)
        self.game._update_score(tie_result)
        assert tie_result == GameResult.TIE
        assert self.game.user_score == 0
        assert self.game.computer_score == 0
        
        # When el usuario gana después
        win_result = self.game.compare_choices(GameChoice.ROCK, GameChoice.SCISSORS)
        self.game._update_score(win_result)
        
        # Then la victoria se registra correctamente
        assert win_result == GameResult.USER_WINS
        assert self.game.user_score == 1
        assert self.game.computer_score == 0

    def test_empate_no_afecta_derrotas_subsecuentes(self):
        """Test: Un empate no afecta las derrotas posteriores."""
        # Given un empate inicial
        tie_result = self.game.compare_choices(GameChoice.PAPER, GameChoice.PAPER)
        self.game._update_score(tie_result)
        assert tie_result == GameResult.TIE
        assert self.game.user_score == 0
        assert self.game.computer_score == 0
        
        # When la computadora gana después
        loss_result = self.game.compare_choices(GameChoice.ROCK, GameChoice.PAPER)
        self.game._update_score(loss_result)
        
        # Then la derrota se registra correctamente
        assert loss_result == GameResult.COMPUTER_WINS
        assert self.game.user_score == 0
        assert self.game.computer_score == 1

    # Test de cobertura completa de empates
    def test_matriz_completa_empates(self):
        """Test: Matriz completa de todos los empates posibles."""
        empates_esperados = [
            (GameChoice.ROCK, GameChoice.ROCK),
            (GameChoice.PAPER, GameChoice.PAPER),
            (GameChoice.SCISSORS, GameChoice.SCISSORS),
            (GameChoice.LIZARD, GameChoice.LIZARD),
            (GameChoice.SPOCK, GameChoice.SPOCK),
        ]
        
        for user_choice, computer_choice in empates_esperados:
            result = self.game.compare_choices(user_choice, computer_choice)
            assert result == GameResult.TIE, \
                f"Empate esperado entre {user_choice} y {computer_choice}"

    # Test de validación de estado del juego
    def test_estado_juego_despues_empate(self):
        """Test: El estado del juego se mantiene correcto después de empates."""
        # Given
        initial_rounds = self.game.rounds_played
        
        # When hay un empate
        result = self.game.compare_choices(GameChoice.SPOCK, GameChoice.SPOCK)
        self.game._update_score(result)
        
        # Then el estado base se mantiene
        assert result == GameResult.TIE
        assert self.game.state == GameState.MENU  # Estado inicial
        assert not self.game._check_game_over()

    # Test de documentación de comportamiento
    def test_empate_preserva_balance_competitivo(self):
        """Test: Los empates preservan el balance competitivo del juego."""
        # Simular un juego con varios empates intercalados
        secuencia_resultados = []
        
        # Empate inicial
        result1 = self.game.compare_choices(GameChoice.ROCK, GameChoice.ROCK)
        self.game._update_score(result1)
        secuencia_resultados.append(result1)
        
        # Victoria usuario
        result2 = self.game.compare_choices(GameChoice.ROCK, GameChoice.SCISSORS)
        self.game._update_score(result2)
        secuencia_resultados.append(result2)
        
        # Empate
        result3 = self.game.compare_choices(GameChoice.PAPER, GameChoice.PAPER)
        self.game._update_score(result3)
        secuencia_resultados.append(result3)
        
        # Victoria computadora
        result4 = self.game.compare_choices(GameChoice.SCISSORS, GameChoice.ROCK)
        self.game._update_score(result4)
        secuencia_resultados.append(result4)
        
        # Verificar secuencia
        assert secuencia_resultados == [
            GameResult.TIE,
            GameResult.USER_WINS,
            GameResult.TIE,
            GameResult.COMPUTER_WINS
        ]
        
        # Verificar marcador final: solo cuentan las victorias, no los empates
        assert self.game.user_score == 1
        assert self.game.computer_score == 1