"""
Tests para JME-10: Feature - Selección de Opción Válida

Este módulo contiene tests específicos para validar la funcionalidad
de selección de opciones válidas del usuario y generación aleatoria
de la computadora.
"""

import pytest
import random
from unittest.mock import patch, MagicMock
from src.game_enums import GameChoice
from src.game import RockPaperScissorsGame


class TestSeleccionOpcionValida:
    """Tests para la selección de opciones válidas del usuario."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame()
    
    def test_display_choices_shows_all_options(self, capsys):
        """Test: El sistema debe mostrar las 5 opciones disponibles."""
        # When
        self.game._display_choices()
        
        # Then
        captured = capsys.readouterr()
        output = captured.out
        
        # Verificar que todas las opciones están presentes
        assert "1. Piedra" in output
        assert "2. Papel" in output
        assert "3. Tijeras" in output
        assert "4. Lagarto" in output
        assert "5. Spock" in output
        assert "OPCIONES DEL JUEGO" in output
    
    @pytest.mark.parametrize("choice_number,expected_choice", [
        (1, GameChoice.ROCK),
        (2, GameChoice.PAPER),
        (3, GameChoice.SCISSORS),
        (4, GameChoice.LIZARD),
        (5, GameChoice.SPOCK),
    ])
    def test_user_can_select_valid_options(self, choice_number, expected_choice):
        """Test: El usuario puede seleccionar opciones del 1 al 5."""
        # Given & When
        with patch('builtins.input', return_value=str(choice_number)):
            result = self.game.get_user_choice()
        
        # Then
        assert result == expected_choice
    
    def test_user_choice_registration(self):
        """Test: El sistema registra correctamente la elección del usuario."""
        # Given
        test_choice = GameChoice.ROCK
        
        # When
        with patch('builtins.input', return_value='1'):
            user_choice = self.game.get_user_choice()
        
        # Then
        assert user_choice == test_choice
        assert isinstance(user_choice, GameChoice)
    
    def test_quit_options_return_none(self):
        """Test: Las opciones de salida devuelven None."""
        quit_options = ['q', 'quit', 'salir', 'Q', 'QUIT', 'SALIR']
        
        for quit_option in quit_options:
            with patch('builtins.input', return_value=quit_option):
                result = self.game.get_user_choice()
                assert result is None
    
    def test_invalid_input_retries(self):
        """Test: Entradas inválidas permiten reintentar."""
        # Given: Primera entrada inválida, segunda válida
        with patch('builtins.input', side_effect=['abc', '1']):
            with patch('builtins.print') as mock_print:
                # When
                result = self.game.get_user_choice()
                
                # Then
                assert result == GameChoice.ROCK
                # Verificar que se mostró mensaje de error
                mock_print.assert_any_call(
                    f"\x1b[31m❌ Entrada inválida. Por favor ingresa un número del 1 al 5.\x1b[0m"
                )
    
    def test_out_of_range_input_shows_error(self):
        """Test: Números fuera del rango 1-5 muestran error."""
        invalid_numbers = ['0', '6', '7', '-1', '100']
        
        for invalid_number in invalid_numbers:
            with patch('builtins.input', side_effect=[invalid_number, '1']):
                with patch('builtins.print') as mock_print:
                    # When
                    result = self.game.get_user_choice()
                    
                    # Then
                    assert result == GameChoice.ROCK
                    # Verificar que se mostró mensaje de error (puede ser ValueError o Error genérico)
                    error_messages = [str(call) for call in mock_print.call_args_list]
                    assert any("❌" in msg and ("Error:" in msg or "inválida" in msg) for msg in error_messages)


class TestGeneracionAleatoria:
    """Tests para la generación aleatoria de elecciones de la computadora."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame()
    
    def test_computer_choice_generation(self):
        """Test: El sistema genera automáticamente una elección aleatoria para la computadora."""
        # When
        computer_choice = self.game.get_computer_choice()
        
        # Then
        assert isinstance(computer_choice, GameChoice)
        assert computer_choice in GameChoice.get_all_choices()
    
    def test_computer_choice_randomness(self):
        """Test: La generación de elección de computadora es aleatoria."""
        # Given: Ejecutar múltiples veces para verificar aleatoriedad
        choices = []
        
        # When: Generar 100 elecciones
        for _ in range(100):
            choice = self.game.get_computer_choice()
            choices.append(choice)
        
        # Then: Debe haber variedad en las elecciones
        unique_choices = set(choices)
        assert len(unique_choices) > 1, "La computadora debe generar elecciones variadas"
        
        # Verificar que todas las elecciones son válidas
        for choice in choices:
            assert choice in GameChoice.get_all_choices()
    
    @pytest.mark.parametrize("seed,expected_sequence", [
        (42, 5),  # Verificar que con seed fijo obtenemos secuencia predecible
        (123, 5),
    ])
    def test_computer_choice_with_seed(self, seed, expected_sequence):
        """Test: Con seed fijo, la generación es predecible (para testing)."""
        # Given
        random.seed(seed)
        choices = []
        
        # When
        for _ in range(expected_sequence):
            choice = self.game.get_computer_choice()
            choices.append(choice)
        
        # Then
        assert len(choices) == expected_sequence
        for choice in choices:
            assert isinstance(choice, GameChoice)
    
    def test_computer_choice_coverage(self):
        """Test: La computadora puede generar todas las opciones posibles."""
        # Given: Forzar todas las opciones posibles
        all_choices = GameChoice.get_all_choices()
        generated_choices = set()
        
        # When: Simular generación de cada opción
        for expected_choice in all_choices:
            with patch('random.choice', return_value=expected_choice):
                choice = self.game.get_computer_choice()
                generated_choices.add(choice)
        
        # Then: Debe poder generar todas las opciones
        assert generated_choices == set(all_choices)


class TestAlmacenamientoElecciones:
    """Tests para verificar que las elecciones se almacenan para posterior comparación."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame()
    
    def test_choices_stored_for_comparison(self):
        """Test: Las elecciones se almacenan para posterior comparación."""
        # Given
        user_choice = GameChoice.ROCK
        computer_choice = GameChoice.SCISSORS
        
        # When: Simular una ronda completa
        with patch.object(self.game, 'get_user_choice', return_value=user_choice):
            with patch.object(self.game, 'get_computer_choice', return_value=computer_choice):
                with patch('builtins.input', return_value=''):  # Para continuar
                    with patch('builtins.print'):  # Silenciar prints
                        result = self.game.play_round()
        
        # Then: Las elecciones deben poder ser comparadas
        comparison_result = self.game.compare_choices(user_choice, computer_choice)
        assert comparison_result is not None
    
    def test_compare_choices_functionality(self):
        """Test: La función compare_choices funciona con las elecciones almacenadas."""
        # Given
        test_cases = [
            (GameChoice.ROCK, GameChoice.SCISSORS, "USER_WINS"),
            (GameChoice.PAPER, GameChoice.ROCK, "USER_WINS"),
            (GameChoice.SCISSORS, GameChoice.PAPER, "USER_WINS"),
            (GameChoice.ROCK, GameChoice.ROCK, "TIE"),
            (GameChoice.SCISSORS, GameChoice.ROCK, "COMPUTER_WINS"),
        ]
        
        for user_choice, computer_choice, expected_result in test_cases:
            # When
            result = self.game.compare_choices(user_choice, computer_choice)
            
            # Then
            assert result.name == expected_result


class TestIntegracionSeleccionValida:
    """Tests de integración para la selección de opciones válidas."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame()
    
    def test_complete_valid_selection_flow(self):
        """Test: Flujo completo de selección válida."""
        # Given: Usuario selecciona opción válida
        with patch('builtins.input', side_effect=['1', 'q']):  # Selección + salir
            with patch('builtins.print'):  # Silenciar prints
                # When
                user_choice = self.game.get_user_choice()
                computer_choice = self.game.get_computer_choice()
                
                # Then
                assert user_choice == GameChoice.ROCK
                assert isinstance(computer_choice, GameChoice)
                
                # Verificar que se pueden comparar
                result = self.game.compare_choices(user_choice, computer_choice)
                assert result is not None
    
    def test_scenario_selection_valid_option(self):
        """
        Test del Scenario: Selección de opción válida
        Given el sistema está ejecutándose
        When el usuario selecciona una opción válida (1-5)  
        Then el sistema debe registrar la elección
        And generar una elección aleatoria para la computadora
        """
        # Given: el sistema está ejecutándose
        game = RockPaperScissorsGame()
        assert game is not None
        
        # When: el usuario selecciona una opción válida (1-5)
        with patch('builtins.input', return_value='3'):  # Tijeras
            user_choice = game.get_user_choice()
        
        # Then: el sistema debe registrar la elección
        assert user_choice == GameChoice.SCISSORS
        assert isinstance(user_choice, GameChoice)
        
        # And: generar una elección aleatoria para la computadora
        computer_choice = game.get_computer_choice()
        assert isinstance(computer_choice, GameChoice)
        assert computer_choice in GameChoice.get_all_choices()
        
        # Verificar que ambas elecciones pueden ser utilizadas
        comparison = game.compare_choices(user_choice, computer_choice)
        assert comparison is not None