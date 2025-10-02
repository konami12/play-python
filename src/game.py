"""
Clase principal del juego Piedra, Papel, Tijeras, Lagarto, Spock

Este módulo contiene la lógica principal del juego implementada
usando Programación Orientada a Objetos.
"""

import random
from typing import Tuple, Optional
from colorama import Fore, Back, Style, init

from .game_enums import GameChoice, GameResult, GameState


class RockPaperScissorsGame:
    """
    Clase principal que maneja la lógica del juego Piedra, Papel, Tijeras, Lagarto, Spock.
    
    Esta clase implementa toda la funcionalidad del juego siguiendo los principios
    de Programación Orientada a Objetos.
    """
    
    def __init__(self, max_score: int = 3):
        """
        Inicializa una nueva instancia del juego.
        
        Args:
            max_score: Puntuación máxima para ganar el juego (default: 3)
        """
        # Inicializar colorama para colores en consola
        init(autoreset=True)
        
        self.max_score = max_score
        self.user_score = 0
        self.computer_score = 0
        self.state = GameState.MENU
        self.rounds_played = 0
        
    def reset_game(self) -> None:
        """Reinicia el juego a su estado inicial."""
        self.user_score = 0
        self.computer_score = 0
        self.state = GameState.MENU
        self.rounds_played = 0
        
    def get_user_choice(self) -> Optional[GameChoice]:
        """
        Obtiene la elección del usuario desde la entrada de consola.
        
        Returns:
            GameChoice o None si el usuario quiere salir
        """
        self._display_choices()
        
        while True:
            try:
                choice_input = input(f"{Fore.CYAN}Selecciona tu opción (1-5, o 'q' para salir): {Style.RESET_ALL}").strip()
                
                if choice_input.lower() in ['q', 'quit', 'salir']:
                    return None
                    
                choice_number = int(choice_input)
                return GameChoice.get_choice_by_number(choice_number)
                
            except ValueError:
                print(f"{Fore.RED}❌ Entrada inválida. Por favor ingresa un número del 1 al 5.{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
    
    def get_computer_choice(self) -> GameChoice:
        """
        Genera una elección aleatoria para la computadora.
        
        Returns:
            GameChoice: Elección aleatoria de la computadora
        """
        return random.choice(GameChoice.get_all_choices())
    
    def compare_choices(self, user_choice: GameChoice, computer_choice: GameChoice) -> GameResult:
        """
        Compara las elecciones del usuario y la computadora para determinar el ganador.
        
        Args:
            user_choice: Elección del usuario
            computer_choice: Elección de la computadora
            
        Returns:
            GameResult: Resultado de la comparación
        """
        if user_choice == computer_choice:
            return GameResult.TIE
        elif user_choice.beats(computer_choice):
            return GameResult.USER_WINS
        else:
            return GameResult.COMPUTER_WINS
    
    def play_round(self) -> bool:
        """
        Juega una ronda completa del juego.
        
        Returns:
            bool: True si se debe continuar el juego, False si se debe salir
        """
        print(f"\n{Back.BLUE}{Fore.WHITE} === RONDA {self.rounds_played + 1} === {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Marcador: Tú {self.user_score} - {self.computer_score} Computadora{Style.RESET_ALL}")
        
        # Obtener elección del usuario
        user_choice = self.get_user_choice()
        if user_choice is None:
            return False  # Usuario quiere salir
            
        # Obtener elección de la computadora
        computer_choice = self.get_computer_choice()
        
        # Mostrar elecciones
        print(f"\n{Fore.GREEN}Tu elección: {user_choice}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Computadora eligió: {computer_choice}{Style.RESET_ALL}")
        
        # Comparar y mostrar resultado
        result = self.compare_choices(user_choice, computer_choice)
        self._display_round_result(result, user_choice, computer_choice)
        
        # Actualizar puntuación
        self._update_score(result)
        
        self.rounds_played += 1
        
        # Verificar si el juego terminó
        if self._check_game_over():
            self._display_final_result()
            return False
            
        return True
    
    def _display_choices(self) -> None:
        """Muestra las opciones disponibles al usuario."""
        print(f"\n{Back.GREEN}{Fore.BLACK} === OPCIONES DEL JUEGO === {Style.RESET_ALL}")
        choices_dict = GameChoice.get_choices_dict()
        
        for number, choice in choices_dict.items():
            print(f"{Fore.CYAN}{number}. {choice}{Style.RESET_ALL}")
    
    def _display_round_result(self, result: GameResult, user_choice: GameChoice, computer_choice: GameChoice) -> None:
        """
        Muestra el resultado de la ronda.
        
        Args:
            result: Resultado de la ronda
            user_choice: Elección del usuario
            computer_choice: Elección de la computadora
        """
        print(f"\n{'-' * 40}")
        
        if result == GameResult.TIE:
            print(f"{Fore.YELLOW}🤝 {result} - Ambos eligieron {user_choice}{Style.RESET_ALL}")
        elif result == GameResult.USER_WINS:
            description = user_choice.get_win_description(computer_choice)
            print(f"{Fore.GREEN}🎉 {result} - {description}{Style.RESET_ALL}")
        else:
            description = computer_choice.get_win_description(user_choice)
            print(f"{Fore.RED}😔 {result} - {description}{Style.RESET_ALL}")
        
        print(f"{'-' * 40}")
    
    def _update_score(self, result: GameResult) -> None:
        """
        Actualiza la puntuación basada en el resultado de la ronda.
        
        Args:
            result: Resultado de la ronda
        """
        if result == GameResult.USER_WINS:
            self.user_score += 1
        elif result == GameResult.COMPUTER_WINS:
            self.computer_score += 1
        # No se actualiza puntuación en caso de empate
    
    def _check_game_over(self) -> bool:
        """
        Verifica si el juego ha terminado.
        
        Returns:
            bool: True si el juego terminó, False en caso contrario
        """
        return self.user_score >= self.max_score or self.computer_score >= self.max_score
    
    def _display_final_result(self) -> None:
        """Muestra el resultado final del juego."""
        print(f"\n{Back.YELLOW}{Fore.BLACK} === JUEGO TERMINADO === {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Marcador Final: Tú {self.user_score} - {self.computer_score} Computadora{Style.RESET_ALL}")
        print(f"Rondas jugadas: {self.rounds_played}")
        
        if self.user_score >= self.max_score:
            print(f"{Fore.GREEN}🏆 ¡FELICITACIONES! ¡Ganaste el juego!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}😔 La computadora ganó este juego. ¡Mejor suerte la próxima vez!{Style.RESET_ALL}")
    
    def display_welcome(self) -> None:
        """Muestra el mensaje de bienvenida."""
        print(f"{Back.CYAN}{Fore.BLACK}")
        print("=" * 60)
        print("   🎮 PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK 🎮")
        print("=" * 60)
        print(f"{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}¡Bienvenido al juego más épico del universo!{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Primer jugador en alcanzar {self.max_score} puntos gana.{Style.RESET_ALL}")
        print()
        
    def display_rules(self) -> None:
        """Muestra las reglas del juego."""
        print(f"{Back.MAGENTA}{Fore.WHITE} === REGLAS DEL JUEGO === {Style.RESET_ALL}")
        print(f"{Fore.CYAN}Piedra{Style.RESET_ALL} aplasta {Fore.CYAN}Tijeras{Style.RESET_ALL} y {Fore.CYAN}Lagarto{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Papel{Style.RESET_ALL} cubre {Fore.CYAN}Piedra{Style.RESET_ALL} y desautoriza {Fore.CYAN}Spock{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Tijeras{Style.RESET_ALL} cortan {Fore.CYAN}Papel{Style.RESET_ALL} y decapitan {Fore.CYAN}Lagarto{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Lagarto{Style.RESET_ALL} come {Fore.CYAN}Papel{Style.RESET_ALL} y envenena {Fore.CYAN}Spock{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Spock{Style.RESET_ALL} aplasta {Fore.CYAN}Tijeras{Style.RESET_ALL} y vaporiza {Fore.CYAN}Piedra{Style.RESET_ALL}")
        print()
    
    def run(self) -> None:
        """Ejecuta el bucle principal del juego."""
        self.display_welcome()
        self.display_rules()
        
        while True:
            if not self.play_round():
                break
                
            # Preguntar si quiere continuar después de cada ronda
            if not self._check_game_over():
                continue_input = input(f"\n{Fore.CYAN}¿Continuar? (Enter para continuar, 'q' para salir): {Style.RESET_ALL}").strip()
                if continue_input.lower() in ['q', 'quit', 'salir']:
                    break
        
        print(f"\n{Fore.YELLOW}¡Gracias por jugar! 🎮✨{Style.RESET_ALL}")