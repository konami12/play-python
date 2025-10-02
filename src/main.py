"""
Punto de entrada principal para el juego Piedra, Papel, Tijeras, Lagarto, Spock

Este módulo proporciona la interfaz de línea de comandos (CLI) para ejecutar el juego.
"""

import sys
import argparse
from colorama import Fore, Style
from .game import RockPaperScissorsGame


def main() -> int:
    """
    Función principal del CLI.
    
    Returns:
        int: Código de salida (0 para éxito, 1 para error)
    """
    parser = argparse.ArgumentParser(
        description="Juego Piedra, Papel, Tijeras, Lagarto, Spock",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python -m src.main                # Juego normal (primero a 3 puntos)
  python -m src.main --score 5      # Juego hasta 5 puntos
  python -m src.main --rules        # Mostrar solo las reglas
  python -m src.main --demo         # Modo demostración
        """
    )
    
    parser.add_argument(
        "--score",
        type=int,
        default=3,
        help="Puntuación máxima para ganar (default: 3)"
    )
    
    parser.add_argument(
        "--rules",
        action="store_true",
        help="Mostrar las reglas del juego y salir"
    )
    
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Ejecutar en modo demostración"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Piedra, Papel, Tijeras, Lagarto, Spock v0.1.0"
    )
    
    try:
        args = parser.parse_args()
        
        # Validar argumentos
        if args.score < 1 or args.score > 10:
            print(f"{Fore.RED}❌ Error: La puntuación debe estar entre 1 y 10{Style.RESET_ALL}")
            return 1
            
        # Mostrar solo reglas si se solicita
        if args.rules:
            game = RockPaperScissorsGame()
            game.display_rules()
            return 0
            
        # Modo demostración
        if args.demo:
            return run_demo_mode()
            
        # Ejecutar juego normal
        game = RockPaperScissorsGame(max_score=args.score)
        game.run()
        
        return 0
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}🎮 Juego interrumpido por el usuario. ¡Hasta luego!{Style.RESET_ALL}")
        return 0
    except Exception as e:
        print(f"{Fore.RED}❌ Error inesperado: {e}{Style.RESET_ALL}")
        return 1


def run_demo_mode() -> int:
    """
    Ejecuta el modo demostración del juego.
    
    Returns:
        int: Código de salida
    """
    from .game_enums import GameChoice
    
    print(f"{Fore.CYAN}🎮 MODO DEMOSTRACIÓN{Style.RESET_ALL}")
    print("=" * 50)
    
    # Mostrar todas las combinaciones posibles
    choices = GameChoice.get_all_choices()
    
    print(f"{Fore.YELLOW}Demostrando todas las reglas del juego:{Style.RESET_ALL}\n")
    
    for choice1 in choices:
        wins_against = []
        for choice2 in choices:
            if choice1.beats(choice2):
                description = choice1.get_win_description(choice2)
                wins_against.append(f"  • {description}")
        
        if wins_against:
            print(f"{Fore.GREEN}{choice1}:{Style.RESET_ALL}")
            for win in wins_against:
                print(win)
            print()
    
    print(f"{Fore.CYAN}¡Demo completada! Usa 'python -m src.main' para jugar.{Style.RESET_ALL}")
    return 0


def run_interactive() -> None:
    """Ejecuta el juego en modo interactivo (sin argumentos de línea de comandos)."""
    try:
        game = RockPaperScissorsGame()
        game.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}🎮 Juego interrumpido. ¡Hasta luego!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    sys.exit(main())