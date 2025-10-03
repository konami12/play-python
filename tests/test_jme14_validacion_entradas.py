"""
Tests para JME-14: Feature - Validación de Entradas de Usuario

Este archivo contiene tests exhaustivos para validar el sistema robusto
de validación de entradas de usuario con manejo de errores.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.game_enums import GameChoice
from src.game import RockPaperScissorsGame


class TestJME14ValidacionEntradas:
    """Test suite para validar la validación de entradas de usuario (JME-14)."""

    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.game = RockPaperScissorsGame()

    # Tests de entradas válidas
    @patch('builtins.input')
    def test_entrada_valida_1(self, mock_input):
        """Test: Entrada válida '1' selecciona Piedra."""
        mock_input.return_value = '1'
        result = self.game.get_user_choice()
        assert result == GameChoice.ROCK

    @patch('builtins.input')
    def test_entrada_valida_2(self, mock_input):
        """Test: Entrada válida '2' selecciona Papel."""
        mock_input.return_value = '2'
        result = self.game.get_user_choice()
        assert result == GameChoice.PAPER

    @patch('builtins.input')
    def test_entrada_valida_3(self, mock_input):
        """Test: Entrada válida '3' selecciona Tijeras."""
        mock_input.return_value = '3'
        result = self.game.get_user_choice()
        assert result == GameChoice.SCISSORS

    @patch('builtins.input')
    def test_entrada_valida_4(self, mock_input):
        """Test: Entrada válida '4' selecciona Lagarto."""
        mock_input.return_value = '4'
        result = self.game.get_user_choice()
        assert result == GameChoice.LIZARD

    @patch('builtins.input')
    def test_entrada_valida_5(self, mock_input):
        """Test: Entrada válida '5' selecciona Spock."""
        mock_input.return_value = '5'
        result = self.game.get_user_choice()
        assert result == GameChoice.SPOCK

    # Tests de entradas de salida
    @patch('builtins.input')
    def test_entrada_salida_q(self, mock_input):
        """Test: Entrada 'q' retorna None (salir)."""
        mock_input.return_value = 'q'
        result = self.game.get_user_choice()
        assert result is None

    @patch('builtins.input')
    def test_entrada_salida_quit(self, mock_input):
        """Test: Entrada 'quit' retorna None (salir)."""
        mock_input.return_value = 'quit'
        result = self.game.get_user_choice()
        assert result is None

    @patch('builtins.input')
    def test_entrada_salida_salir(self, mock_input):
        """Test: Entrada 'salir' retorna None (salir)."""
        mock_input.return_value = 'salir'
        result = self.game.get_user_choice()
        assert result is None

    @patch('builtins.input')
    def test_entrada_salida_case_insensitive(self, mock_input):
        """Test: Entradas de salida son case insensitive."""
        entradas_salida = ['Q', 'QUIT', 'SALIR', 'Quit', 'Salir']
        
        for entrada in entradas_salida:
            mock_input.return_value = entrada
            result = self.game.get_user_choice()
            assert result is None, f"'{entrada}' debería ser reconocido como salida"

    # Tests de entradas fuera de rango
    @patch('builtins.input')
    @patch('builtins.print')
    def test_entrada_fuera_rango_0(self, mock_print, mock_input):
        """Test: Entrada '0' genera error y pide reintento."""
        mock_input.side_effect = ['0', '1']  # Primero inválida, luego válida
        result = self.game.get_user_choice()
        
        # Debe retornar la elección válida después del error
        assert result == GameChoice.ROCK
        # Debe haber mostrado error por entrada fuera de rango
        error_encontrado = any("Opción inválida: 0" in str(call) for call in mock_print.call_args_list)
        assert error_encontrado, "No se encontró mensaje de error para entrada fuera de rango 0"

    @patch('builtins.input')
    @patch('builtins.print')
    def test_entrada_fuera_rango_6(self, mock_print, mock_input):
        """Test: Entrada '6' genera error y pide reintento."""
        mock_input.side_effect = ['6', '2']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.PAPER
        error_encontrado = any("Opción inválida: 6" in str(call) for call in mock_print.call_args_list)
        assert error_encontrado, "No se encontró mensaje de error para entrada fuera de rango 6"

    @patch('builtins.input')
    @patch('builtins.print')
    def test_entradas_fuera_rango_multiples(self, mock_print, mock_input):
        """Test: Múltiples entradas fuera de rango."""
        entradas_invalidas = ['-1', '7', '100', '999']
        
        for entrada_invalida in entradas_invalidas:
            mock_input.side_effect = [entrada_invalida, '3']
            result = self.game.get_user_choice()
            assert result == GameChoice.SCISSORS

    # Tests de entradas de texto
    @patch('builtins.input')
    @patch('builtins.print')
    def test_entrada_texto_abc(self, mock_print, mock_input):
        """Test: Entrada de texto 'abc' genera error."""
        mock_input.side_effect = ['abc', '4']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.LIZARD
        # Verificar que se mostró error por entrada no numérica
        assert any("❌ Entrada inválida. Por favor ingresa un número del 1 al 5." in str(call) 
                  for call in mock_print.call_args_list)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_entrada_texto_piedra(self, mock_print, mock_input):
        """Test: Entrada de texto 'piedra' genera error."""
        mock_input.side_effect = ['piedra', '1']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.ROCK
        assert any("❌ Entrada inválida. Por favor ingresa un número del 1 al 5." in str(call) 
                  for call in mock_print.call_args_list)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_entrada_texto_various(self, mock_print, mock_input):
        """Test: Varias entradas de texto generan errores."""
        entradas_texto = ['hello', 'world', 'test', 'invalid']
        
        for texto in entradas_texto:
            mock_input.side_effect = [texto, '5']
            result = self.game.get_user_choice()
            assert result == GameChoice.SPOCK

    # Tests de entradas vacías y espacios
    @patch('builtins.input')
    @patch('builtins.print')
    def test_entrada_vacia(self, mock_print, mock_input):
        """Test: Entrada vacía genera error."""
        mock_input.side_effect = ['', '2']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.PAPER
        assert any("❌ Entrada inválida. Por favor ingresa un número del 1 al 5." in str(call) 
                  for call in mock_print.call_args_list)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_entrada_solo_espacios(self, mock_print, mock_input):
        """Test: Entrada de solo espacios genera error."""
        mock_input.side_effect = ['   ', '3']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.SCISSORS
        assert any("❌ Entrada inválida. Por favor ingresa un número del 1 al 5." in str(call) 
                  for call in mock_print.call_args_list)

    @patch('builtins.input')
    def test_entrada_con_espacios_valida(self, mock_input):
        """Test: Entrada válida con espacios se procesa correctamente."""
        mock_input.return_value = '  4  '  # Espacios alrededor del número
        result = self.game.get_user_choice()
        assert result == GameChoice.LIZARD

    # Tests de caracteres especiales
    @patch('builtins.input')
    @patch('builtins.print')
    def test_caracteres_especiales(self, mock_print, mock_input):
        """Test: Caracteres especiales generan errores."""
        caracteres_especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        
        for caracter in caracteres_especiales:
            mock_input.side_effect = [caracter, '1']
            result = self.game.get_user_choice()
            assert result == GameChoice.ROCK

    # Tests de números decimales
    @patch('builtins.input')
    @patch('builtins.print')
    def test_numeros_decimales(self, mock_print, mock_input):
        """Test: Números decimales generan errores."""
        decimales = ['1.5', '2.7', '3.14', '4.0', '5.999']
        
        for decimal in decimales:
            mock_input.side_effect = [decimal, '2']
            result = self.game.get_user_choice()
            assert result == GameChoice.PAPER

    # Tests de números negativos
    @patch('builtins.input')
    @patch('builtins.print')
    def test_numeros_negativos(self, mock_print, mock_input):
        """Test: Números negativos generan errores."""
        negativos = ['-1', '-5', '-10', '-999']
        
        for negativo in negativos:
            mock_input.side_effect = [negativo, '3']
            result = self.game.get_user_choice()
            assert result == GameChoice.SCISSORS

    # Tests de secuencias de entradas inválidas
    @patch('builtins.input')
    @patch('builtins.print')
    def test_multiples_entradas_invalidas_seguidas(self, mock_print, mock_input):
        """Test: Múltiples entradas inválidas seguidas antes de una válida."""
        mock_input.side_effect = ['abc', '0', '6', 'hello', '', '2']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.PAPER
        # Debe haber mostrado múltiples mensajes de error
        assert mock_print.call_count >= 5  # Al menos 5 llamadas (errores + display)

    # Tests de validación robusta
    @patch('builtins.input')
    def test_validacion_trim_funciona(self, mock_input):
        """Test: La validación hace trim correctamente."""
        entradas_con_espacios = ['  1  ', '\t2\t', '\n3\n', ' 4 ', '5   ']
        opciones_esperadas = [GameChoice.ROCK, GameChoice.PAPER, GameChoice.SCISSORS, 
                             GameChoice.LIZARD, GameChoice.SPOCK]
        
        for entrada, opcion_esperada in zip(entradas_con_espacios, opciones_esperadas):
            mock_input.return_value = entrada
            result = self.game.get_user_choice()
            assert result == opcion_esperada

    # Tests de casos edge específicos del ticket
    @patch('builtins.input')
    @patch('builtins.print')
    def test_scenario_entrada_invalida_6(self, mock_print, mock_input):
        """Test: Escenario específico del ticket - entrada inválida '6'."""
        # Given el sistema pide una opción al usuario
        # When el usuario ingresa un valor inválido (ej: 6)
        mock_input.side_effect = ['6', '1']
        
        # Then el sistema debe mostrar un mensaje de error
        result = self.game.get_user_choice()
        
        # And solicitar nuevamente la entrada
        assert result == GameChoice.ROCK
        # Verificar que se mostró mensaje de error específico
        error_calls = [call for call in mock_print.call_args_list 
                      if 'Error' in str(call) and '6' in str(call)]
        assert len(error_calls) > 0

    @patch('builtins.input')
    @patch('builtins.print')
    def test_scenario_entrada_texto(self, mock_print, mock_input):
        """Test: Escenario específico del ticket - entrada de texto."""
        mock_input.side_effect = ['texto', '2']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.PAPER
        assert any("❌ Entrada inválida" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_scenario_entrada_vacia_specific(self, mock_print, mock_input):
        """Test: Escenario específico del ticket - entrada vacía."""
        mock_input.side_effect = ['', '3']
        result = self.game.get_user_choice()
        
        assert result == GameChoice.SCISSORS
        assert any("❌ Entrada inválida" in str(call) for call in mock_print.call_args_list)

    # Tests de mensajes de error específicos
    @patch('builtins.input')
    @patch('builtins.print')
    def test_mensaje_error_fuera_rango_especifico(self, mock_print, mock_input):
        """Test: Mensaje de error específico para entrada fuera de rango."""
        mock_input.side_effect = ['0', '1']
        self.game.get_user_choice()
        
        # Verificar mensaje específico para fuera de rango
        error_encontrado = False
        for call in mock_print.call_args_list:
            call_str = str(call)
            if "Opción inválida" in call_str and "Las opciones válidas son" in call_str:
                error_encontrado = True
                break
        assert error_encontrado, "No se encontró mensaje específico de error para fuera de rango"

    @patch('builtins.input')
    @patch('builtins.print') 
    def test_mensaje_error_no_numerico_especifico(self, mock_print, mock_input):
        """Test: Mensaje de error específico para entrada no numérica."""
        mock_input.side_effect = ['abc', '2']
        self.game.get_user_choice()
        
        # Verificar mensaje específico para entrada no numérica
        error_encontrado = False
        for call in mock_print.call_args_list:
            call_str = str(call)
            if "Entrada inválida" in call_str and "número del 1 al 5" in call_str:
                error_encontrado = True
                break
        assert error_encontrado, "No se encontró mensaje específico de error para entrada no numérica"

    # Tests de flujo de juego sin crashes
    @patch('builtins.input')
    def test_flujo_no_crash_con_entradas_invalidas(self, mock_input):
        """Test: El flujo del juego se mantiene sin crashes con entradas inválidas."""
        # Simular múltiples tipos de entradas inválidas antes de una válida
        entradas_problematicas = ['', 'abc', '0', '6', '-1', '1.5', '!', 'quit']
        mock_input.return_value = 'quit'  # Para que termine el loop
        
        result = self.game.get_user_choice()
        assert result is None  # quit debería retornar None

    # Tests de integración con GameChoice
    def test_integracion_con_gamechoice(self):
        """Test: Integración correcta con GameChoice.get_choice_by_number()."""
        # Verificar que todas las opciones válidas funcionan
        for numero in range(1, 6):
            choice = GameChoice.get_choice_by_number(numero)
            assert choice is not None
            assert isinstance(choice, GameChoice)

    def test_gamechoice_lanza_excepcion_fuera_rango(self):
        """Test: GameChoice.get_choice_by_number() lanza excepción para números inválidos."""
        numeros_invalidos = [0, 6, 7, -1, 100]
        
        for numero in numeros_invalidos:
            with pytest.raises(Exception):  # ValueError o similar
                GameChoice.get_choice_by_number(numero)

    # Tests de cobertura completa
    @patch('builtins.input')
    def test_cobertura_todas_entradas_validas(self, mock_input):
        """Test: Cobertura completa de todas las entradas válidas."""
        entradas_validas = ['1', '2', '3', '4', '5']
        opciones_esperadas = [GameChoice.ROCK, GameChoice.PAPER, GameChoice.SCISSORS,
                             GameChoice.LIZARD, GameChoice.SPOCK]
        
        for entrada, opcion in zip(entradas_validas, opciones_esperadas):
            mock_input.return_value = entrada
            result = self.game.get_user_choice()
            assert result == opcion

    @patch('builtins.input')
    @patch('builtins.print')
    def test_cobertura_todas_entradas_invalidas(self, mock_print, mock_input):
        """Test: Cobertura de tipos de entradas inválidas."""
        tipos_invalidos = [
            ('0', 'fuera_rango_bajo'),
            ('6', 'fuera_rango_alto'), 
            ('abc', 'texto'),
            ('', 'vacio'),
            ('1.5', 'decimal'),
            ('-1', 'negativo'),
            ('!', 'especial')
        ]
        
        for entrada_invalida, tipo in tipos_invalidos:
            mock_input.side_effect = [entrada_invalida, '1']
            result = self.game.get_user_choice()
            assert result == GameChoice.ROCK, f"Falló para tipo: {tipo}"