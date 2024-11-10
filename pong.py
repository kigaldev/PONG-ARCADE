import turtle
import time

class PongGame:
    def __init__(self):
        # Configuración de la pantalla
        self.screen = turtle.Screen()
        self.screen.title("Pong - Arcade Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)  # Pantalla más grande para mejor jugabilidad
        self.screen.tracer(0)
        
        # Configuración inicial
        self.PADDLE_SPEED = 20
        self.BALL_SPEED = 1.5
        self.SPEED_INCREMENT = 2
        self.COLLISION_THRESHOLD = 5
        
        self.init_game_objects()
        self.init_score()
        self.bind_keys()
        
        # Variables de estado
        self.game_paused = False
        self.collision_count = 0
        
    def init_game_objects(self):
        # Inicializar paletas
        self.paddles = {}
        for side, x_pos in [("left", -350), ("right", 350)]:
            paddle = turtle.Turtle()
            paddle.speed(0)
            paddle.shape("square")
            paddle.color("white")
            paddle.shapesize(stretch_wid=6, stretch_len=1)
            paddle.penup()
            paddle.goto(x_pos, 0)
            self.paddles[side] = paddle
            
        # Inicializar pelota
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.reset_ball()
        
    def init_score(self):
        self.score = {"left": 0, "right": 0}
        self.score_display = turtle.Turtle()
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.update_score()
        
    def bind_keys(self):
        self.screen.listen()
        # Controles de las paletas
        self.screen.onkeypress(lambda: self.move_paddle("left", "up"), "w")
        self.screen.onkeypress(lambda: self.move_paddle("left", "down"), "s")
        self.screen.onkeypress(lambda: self.move_paddle("right", "up"), "Up")
        self.screen.onkeypress(lambda: self.move_paddle("right", "down"), "Down")
        # Controles adicionales
        self.screen.onkey(self.toggle_pause, "space")
        self.screen.onkey(self.reset_game, "r")
        
    def move_paddle(self, side, direction):
        paddle = self.paddles[side]
        current_y = paddle.ycor()
        new_y = current_y + (self.PADDLE_SPEED if direction == "up" else -self.PADDLE_SPEED)
        
        # Limitar movimiento dentro de la pantalla
        if -250 < new_y < 250:
            paddle.sety(new_y)
            
    def reset_ball(self):
        self.ball.goto(0, 0)
        self.ball.dx = self.BALL_SPEED
        self.ball.dy = self.BALL_SPEED
        self.collision_count = 0
        
    def update_score(self):
        self.score_display.clear()
        score_text = f"Jugador Izquierdo: {self.score['left']}  Jugador Derecho: {self.score['right']}"
        self.score_display.write(score_text, align="center", font=("Courier", 16, "normal"))
        
    def check_collisions(self):
        # Colisiones con bordes superior e inferior
        if abs(self.ball.ycor()) > 290:
            self.ball.dy *= -1
            
        # Colisiones con paletas
        for side, paddle in self.paddles.items():
            if (abs(self.ball.xcor() - paddle.xcor()) < 20 and 
                abs(self.ball.ycor() - paddle.ycor()) < 50):
                self.ball.dx *= -1
                self.collision_count += 1
                
                # Incrementar velocidad después de cierto número de colisiones
                if self.collision_count >= self.COLLISION_THRESHOLD:
                    self.ball.dx *= self.SPEED_INCREMENT
                    self.ball.dy *= self.SPEED_INCREMENT
                    self.collision_count = 0
                    
    def check_scoring(self):
        # Puntuación
        if self.ball.xcor() > 390:
            self.score["left"] += 1
            self.update_score()
            self.reset_ball()
        elif self.ball.xcor() < -390:
            self.score["right"] += 1
            self.update_score()
            self.reset_ball()
            
    def toggle_pause(self):
        self.game_paused = not self.game_paused
        
    def reset_game(self):
        self.score = {"left": 0, "right": 0}
        self.update_score()
        self.reset_ball()
        
    def run(self):
        while True:
            self.screen.update()
            
            if not self.game_paused:
                # Mover la pelota
                self.ball.setx(self.ball.xcor() + self.ball.dx)
                self.ball.sety(self.ball.ycor() + self.ball.dy)
                
                self.check_collisions()
                self.check_scoring()
                
            time.sleep(1/120)  # Limitar FPS para consistencia

if __name__ == "__main__":
    game = PongGame()
    game.run()
    