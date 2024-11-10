import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Pong - Arcade Game")
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.tracer(0)  # Desactiva la actualización automática para control manual

# Paleta del Jugador Izquierdo
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-250, 0)

# Paleta del Jugador Derecho
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

# Pelota
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1  # Velocidad en el eje x
ball.dy = 0.1  # Velocidad en el eje y

# Puntuación
score_left = 0
score_right = 0

# Contador de colisiones con las paletas
collision_count = 0
collision_threshold = 5  # Incrementar velocidad cada 5 colisiones

# Mostrar puntuación
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 160)
score_display.write("Jugador Izquierdo: 0  Jugador Derecho: 0", align="center", font=("Courier", 14, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Jugador Izquierdo: {score_left}  Jugador Derecho: {score_right}", align="center", font=("Courier", 14, "normal"))

# Funciones de movimiento de paletas
def move_left_paddle_up():
    y = left_paddle.ycor()
    if y < 150:  # Limita el movimiento
        left_paddle.sety(y + 20)

def move_left_paddle_down():
    y = left_paddle.ycor()
    if y > -150:
        left_paddle.sety(y - 20)

def move_right_paddle_up():
    y = right_paddle.ycor()
    if y < 150:
        right_paddle.sety(y + 20)

def move_right_paddle_down():
    y = right_paddle.ycor()
    if y > -150:
        right_paddle.sety(y - 20)

# Asignación de teclas
screen.listen()
screen.onkeypress(move_left_paddle_up, "w")
screen.onkeypress(move_left_paddle_down, "s")
screen.onkeypress(move_right_paddle_up, "Up")
screen.onkeypress(move_right_paddle_down, "Down")

# Bucle principal del juego
while True:
    screen.update()
    
    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Colisiones con los bordes superior e inferior
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1
    
    # Colisión con la paleta derecha
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.dx *= -1
    
    # Colisión con la paleta izquierda
    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.dx *= -1
    
    # Incrementa la velocidad de la pelota cada 10 colisiones
    if collision_count >= collision_threshold:
        ball.dx *= 1.1
        ball.dy *= 1.1
        collision_count = 0  # Reinicia el contador
        
    # Revisión de puntos para el Jugador Derecho
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        update_score()
    
    # Revisión de puntos para el Jugador Izquierdo
    elif ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        update_score()
