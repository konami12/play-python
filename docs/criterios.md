📌 Criterios de Aceptación (Gherkin)
Feature: Jugar Piedra, Papel, Tijeras, Lagarto, Spock
Feature: Juego de Piedra, Papel, Tijeras, Lagarto, Spock
  Como jugador
  Quiero jugar contra la computadora
  Para competir y determinar un ganador.

  Scenario: Selección de opción válida
    Given el sistema está ejecutándose
    When el usuario selecciona una opción válida (1-5)
    Then el sistema debe registrar la elección
    And generar una elección aleatoria para la computadora

  Scenario: Resultado de una ronda - Victoria del usuario
    Given el usuario selecciona "Piedra"
    And la computadora selecciona "Tijeras"
    When se comparan las elecciones
    Then el usuario debe ganar la ronda
    And el marcador del usuario debe aumentar en 1

  Scenario: Resultado de una ronda - Empate
    Given el usuario selecciona "Lagarto"
    And la computadora selecciona "Lagarto"
    When se comparan las elecciones
    Then debe declararse empate
    And el marcador no debe cambiar

  Scenario: Finalización del juego
    Given el marcador del usuario es 2
    And el marcador de la computadora es 2
    When el usuario gana la siguiente ronda
    Then el juego debe terminar
    And el sistema debe mostrar "Ganaste el juego"

  Scenario: Validación de entradas
    Given el sistema pide una opción al usuario
    When el usuario ingresa un valor inválido (ej: 6, texto, vacío)
    Then el sistema debe mostrar un mensaje de error
    And solicitar nuevamente la entrada