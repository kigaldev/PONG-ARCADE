# 🎮 Pong Arcade Game

> ¡Revive el clásico juego arcade **Pong** en Python!

Este proyecto recrea el famoso juego Pong utilizando el módulo `turtle` de Python. Desafía a un amigo y compite para ver quién logra mantener la pelota en juego más tiempo. ¡Simple, divertido y retro!

---

## 📂 Estructura del Proyecto

- **`pong.py`**: Contiene el código principal del juego.
- **`README.md`**: Documentación general del proyecto.
- **`requirements.txt`**: Lista de dependencias necesarias (opcional).
- **`assets/`**: Carpeta para incluir recursos adicionales como sonidos o gráficos (vacía por defecto).

---

## 🚀 Instalación

1. **Clona el repositorio**:

   git clone https://github.com/tu-usuario/pong-arcade-game.git
   cd pong-arcade-game
Configura el entorno:

Asegúrate de tener Python 3.6 o superior instalado en tu sistema.
Instala las dependencias en requirements.txt (si existen).
Ejecuta el juego:


python pong.py
🎮 Controles del Juego
Jugador	Acción	Tecla
Izquierdo	Mover arriba	W
Izquierdo	Mover abajo	S
Derecho	Mover arriba	↑ (flecha)
Derecho	Mover abajo	↓ (flecha)
🔍 Lógica de Programación
El juego se basa en una lógica sencilla y clara, diseñada para una experiencia de juego fluida:

Configuración del Entorno:

Crea una pantalla de 600x400 píxeles.
Configura las paletas para cada jugador y la pelota.
Movimiento de la Pelota:

La pelota se mueve en diagonal y rebota en los bordes superior e inferior de la pantalla.
Colisiones:

La pelota rebota al tocar las paletas o los bordes superior/inferior de la pantalla.
Cuando un jugador no logra golpear la pelota, el jugador contrario suma un punto.
Puntuación:

Cada vez que la pelota sale por un extremo, el jugador opuesto gana un punto.
La pelota se reinicia en el centro para continuar el juego.
📜 Créditos
Proyecto inspirado en el clásico juego Pong. Este código es una práctica en Python para reforzar conceptos de programación de videojuegos simples.