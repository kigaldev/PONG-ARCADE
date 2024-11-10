# Instrucciones del Proyecto: Pong Arcade Game

Este archivo contiene una explicación detallada del juego, cómo funciona el código y algunas ideas para extender el proyecto.

---

## 🎮 Descripción del Juego

Pong es un juego de tenis de mesa clásico en el que dos jugadores controlan paletas verticales y tratan de evitar que la pelota salga de su lado de la pantalla. En esta versión, el jugador izquierdo usa las teclas `W` y `S` para mover su paleta, mientras que el jugador derecho usa las flechas `↑` y `↓`.

---

## 📋 Cómo Jugar

1. **Ejecuta el archivo** `pong.py` siguiendo las instrucciones del archivo `README.md`.
2. **Controles**:
   - **Jugador Izquierdo**: Mueve la paleta con las teclas `W` (arriba) y `S` (abajo).
   - **Jugador Derecho**: Mueve la paleta con las flechas `↑` (arriba) y `↓` (abajo).
3. **Objetivo**: Evitar que la pelota pase tu borde de la pantalla y ganar puntos cuando el oponente falla en golpear la pelota.

---

## 🔍 Explicación de la Lógica del Código

El archivo `pong.py` utiliza el módulo `turtle` de Python para crear y gestionar gráficos y objetos en pantalla. Aquí tienes una explicación detallada de los componentes principales:

### 1. Configuración de la Pantalla
   - La pantalla del juego se crea con dimensiones de **600x400** píxeles, un fondo negro y el título "Pong - Arcade Game".
   - La pantalla usa `screen.tracer(0)` para controlar manualmente las actualizaciones, lo que mejora el rendimiento.

### 2. Creación de Objetos
   - **Paletas**: Se crean dos paletas con una forma rectangular, cada una posicionada en lados opuestos de la pantalla.
   - **Pelota**: La pelota es un círculo blanco que comienza en el centro y se mueve en diagonal.

### 3. Movimiento de la Pelota
   - La pelota tiene una velocidad `dx` y `dy`, que controlan su dirección en los ejes `x` e `y`.
   - La pelota rebota en los bordes superior e inferior cambiando la dirección de `dy`.

### 4. Colisiones con Paletas
   - La pelota verifica su posición y si toca una paleta, cambia su dirección en `dx`.
   - Si la pelota pasa el borde izquierdo o derecho, el jugador opuesto gana un punto y la pelota se reinicia en el centro.

### 5. Sistema de Puntuación
   - Cada jugador gana puntos cuando el oponente falla. La puntuación se muestra en la parte superior de la pantalla y se actualiza cada vez que cambia.
