# 🎮 Piedra, Papel, Tijeras, Lagarto, Spock

Un juego interactivo de consola desarrollado en Python que implementa la versión extendida del clásico juego "Piedra, Papel, Tijeras" popularizada por la serie "The Big Bang Theory".

## 📋 Descripción

Este proyecto implementa el juego "Piedra, Papel, Tijeras, Lagarto, Spock" usando Python 3.12+ con una arquitectura orientada a objetos, colores en consola y una interfaz de línea de comandos completa.

## 🎯 Características

- ✅ **5 opciones de juego**: Piedra, Papel, Tijeras, Lagarto, Spock
- ✅ **Interfaz colorida**: Uso de colorama para colores en consola
- ✅ **Arquitectura POO**: Clases y Enums bien estructurados
- ✅ **CLI completa**: Argumentos de línea de comandos
- ✅ **Validación robusta**: Manejo de errores y entradas inválidas
- ✅ **Tests completos**: Suite de tests con pytest
- ✅ **Código limpio**: Siguiendo PEP 8 y buenas prácticas

## 🏗️ Estructura del Proyecto

```
ProyectoIA/
├── src/                      # Código fuente principal
│   ├── __init__.py          # Configuración del paquete
│   ├── __main__.py          # Entrada del módulo
│   ├── main.py              # CLI principal
│   ├── game.py              # Lógica principal del juego
│   └── game_enums.py        # Enumeraciones del juego
├── tests/                   # Tests unitarios
│   ├── __init__.py
│   └── test_game_setup.py   # Tests de configuración
├── docs/                    # Documentación
│   ├── stack.md            # Stack tecnológico
│   └── criterios.md        # Criterios de aceptación
├── requirements.txt         # Dependencias
├── pyproject.toml          # Configuración de herramientas
├── .gitignore              # Archivos ignorados por git
└── README.md               # Este archivo
```

## 🛠️ Stack Tecnológico

- **Lenguaje**: Python 3.12+
- **Gestión de dependencias**: pip
- **Librerías**: colorama (colores en consola)
- **Paradigma**: Programación Orientada a Objetos + Enum
- **Ejecución**: CLI (Command Line Interface)
- **Control de versiones**: Git
- **Pruebas**: pytest

## 🚀 Instalación

### Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ProyectoIA
   ```

2. **Crear entorno virtual** (recomendado):
   ```bash
   python3 -m venv venv
   
   # En macOS/Linux:
   source venv/bin/activate
   
   # En Windows:
   venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Uso

### Ejecución Básica

```bash
# Juego normal (primero a 3 puntos)
python -m src

# Juego personalizado (hasta 5 puntos)
python -m src.main --score 5

# Mostrar solo las reglas
python -m src.main --rules

# Modo demostración
python -m src.main --demo

# Mostrar ayuda
python -m src.main --help
```

### Opciones del CLI

```
usage: main.py [-h] [--score SCORE] [--rules] [--demo] [--version]

Juego Piedra, Papel, Tijeras, Lagarto, Spock

options:
  -h, --help     show this help message and exit
  --score SCORE  Puntuación máxima para ganar (default: 3)
  --rules        Mostrar las reglas del juego y salir
  --demo         Ejecutar en modo demostración
  --version      show program's version number and exit
```

## 📖 Reglas del Juego

El juego extiende el clásico "Piedra, Papel, Tijeras" con dos opciones adicionales:

- **Piedra** aplasta **Tijeras** y **Lagarto**
- **Papel** cubre **Piedra** y desautoriza **Spock**
- **Tijeras** cortan **Papel** y decapitan **Lagarto**
- **Lagarto** come **Papel** y envenena **Spock**
- **Spock** aplasta **Tijeras** y vaporiza **Piedra**

### Cómo Jugar

1. Ejecuta el juego con `python -m src`
2. Selecciona una opción (1-5) cuando se te solicite
3. El primer jugador en alcanzar la puntuación objetivo (default: 3) gana
4. Usa 'q' para salir en cualquier momento

## 🧪 Testing

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Tests con cobertura
pytest --cov=src --cov-report=html

# Tests específicos
pytest tests/test_game_setup.py

# Tests en modo verbose
pytest -v
```

### Tipos de Tests Incluidos

- **Tests de setup**: Validación del stack tecnológico
- **Tests de enums**: Verificación de enumeraciones
- **Tests de lógica**: Validación de reglas del juego
- **Tests de inicialización**: Configuración del juego

## 🛠️ Desarrollo

### Herramientas de Calidad de Código

```bash
# Formateo de código
black src/ tests/
isort src/ tests/

# Linting
flake8 src/ tests/

# Verificación de tipos
mypy src/
```

### Estructura de Clases Principales

- **`GameChoice`**: Enum con las 5 opciones del juego
- **`GameResult`**: Enum para resultados de rondas
- **`GameState`**: Enum para estados del juego
- **`RockPaperScissorsGame`**: Clase principal del juego

## 🎯 Características Técnicas

### Enum GameChoice

```python
from src.game_enums import GameChoice

# Obtener opción por número
choice = GameChoice.get_choice_by_number(1)  # ROCK

# Verificar victoria
rock_wins = GameChoice.ROCK.beats(GameChoice.SCISSORS)  # True

# Descripción de victoria
desc = GameChoice.ROCK.get_win_description(GameChoice.SCISSORS)
# "Piedra aplasta Tijeras"
```

### Clase Principal

```python
from src.game import RockPaperScissorsGame

# Crear juego
game = RockPaperScissorsGame(max_score=5)

# Ejecutar
game.run()

# Reiniciar
game.reset_game()
```

## 🐛 Troubleshooting

### Problemas Comunes

1. **Error de importación de colorama**:
   ```bash
   pip install colorama
   ```

2. **Python no encontrado**:
   - Verificar que Python 3.12+ esté instalado
   - Usar `python3` en lugar de `python`

3. **Tests fallan**:
   ```bash
   pip install pytest pytest-cov
   ```

## 🔄 Roadmap

- [ ] Modo multijugador
- [ ] Guardado de estadísticas
- [ ] Interfaz gráfica (GUI)
- [ ] Torneos y rankings
- [ ] Sonidos y efectos

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Hacer commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🙏 Créditos

- Juego original inspirado en "The Big Bang Theory"
- Desarrollado como proyecto educativo
- Stack tecnológico basado en especificaciones de `docs/stack.md`

---

**¡Que la fuerza (y Spock) te acompañen! 🖖✨**