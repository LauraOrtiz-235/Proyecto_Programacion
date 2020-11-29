import pygame, random
from menu import Menu

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (50,230,70)
RED = (250,20,20)

class Game(object):
    def __init__(self):
        # Crear nuevo objeto: fuente
        self.font = pygame.font.Font(None,60)
        # Crear la fuente para el mensaje de la puntuación final
        self.font_1 = pygame.font.Font("Triforce.TTF",28)
        # Crear la fuente de letra para el mensaje del score
        self.score_font = pygame.font.Font("Kenvector.TTF",25)
        # Crear la fuente de letra para el mensaje de la vida del covid
        self.life_font = pygame.font.Font("Kenvector.TTF",25)
        # Crear un diccionario con llaves: num1, num2, result
        # Estas variables se van a usar para crear los problemas matemáticos
        self.problem = {"num1":0,"num2":0,"result":0}
        # Crear una variable que guarda el nombre de la operación
        self.operation = ""
        self.symbols = self.get_symbols()
        self.button_list = self.get_button_list()
        self.reset_problem = False
        # Crear menu
        items = ("Easy","Medium","Hard","Presented")
        self.menu = Menu(items,ttf_font="Kenvector.TTF",font_size=30)
        # True: muestra el menu
        self.show_menu = True
        # Crear el contador del puntaje
        self.score = 0
        # Crear el contador de vida del covid
        self.life = 100
        # Contar el número de problemas (preguntas)
        self.count = 0
        # Cargar la imagen de fondo
        self.background_image = pygame.image.load("fondo_game.jpg").convert()
        # Cargar los efectos de sonido
        self.sound_1 = pygame.mixer.Sound("correcto.ogg")
        self.sound_2 = pygame.mixer.Sound("incorrecto.ogg")
        # Crear la variable donde depende el nivel 
        self.level = 0


    def get_button_list(self):
        #Devuelve una lista de los cuatro botones 
        button_list = []
        # Se asigna uno de los botones como la respuesta correcta
        choice = random.randint(1,4)
        # Definir el ancho y el alto de los botones
        width = 100
        height = 100
        # t_w: la definimos como el "ancho total"
        t_w = width * 2 + 50
        # Definimos las posiciones
        posX = (SCREEN_WIDTH / 2) - (t_w /2)
        posY = 200

        if choice == 1:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(10,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150

        if choice == 2:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(10,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w /2)
        posY = 300

        if choice == 3:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(10,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150

        if choice == 4:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(10,100))
            button_list.append(btn)

        return button_list


    def get_image(self,sprite,x,y,width,height):
        #Este método corta las imagenes y las devuleve
        # Crear una imagen en blanco
        image = pygame.Surface([width,height]).convert()
        # Copiar el sprite de un hoja mñas grande a una más pequeña
        image.blit(sprite,(0,0),(x,y,width,height))
        # Retornar la imagen
        return image


    def get_symbols(self):
        #Retornar un diccionario con los símbolos de operación recortados de la imagen
        symbols = {}
        sprite = pygame.image.load("symbols.png").convert()
        image = self.get_image(sprite,0,0,64,64)
        symbols["addition"] = image
        image = self.get_image(sprite,64,0,64,64)
        symbols["subtraction"] = image
        image = self.get_image(sprite,128,0,64,64)
        symbols["multiplication"] = image
        image = self.get_image(sprite,192,0,64,64)
        symbols["division"] = image

        return symbols


    #En las siguientes definiciones se establecen las operaciones
    #Y se utiliza random.randint para obtener los numeros random
    def easy_level(self):
        #Se define las operaciones de suma y resta
        #Establece num1,num2 y el resultado para el nivel 1 
        ops = random.randint(1,2)
        a = random.randint(0,100)
        b = random.randint(0,100)

        self.problem["num1"] = a
        self.problem["num2"] = b

        if ops == 1:
            self.problem["result"] = a + b
            self.operation = "addition"

        else:
            if a > b:
                self.problem["result"] = a - b
            else:
                self.problem["num1"] = b
                self.problem["num2"] = a
                self.problem["result"] = b - a
            self.operation = "subtraction"


    def medium_level(self):
        #Se define las operaciones de suma, resta y multiplicación
        #Establece num1,num2 y el resultado para el nivel 2
        ops = random.randint(1,6)
        a = random.randint(0,100)
        b = random.randint(0,100)

        self.problem["num1"] = a
        self.problem["num2"] = b

        if (ops == 1) or (ops == 4):
            self.problem["result"] = a + b
            self.operation = "addition"

        elif (ops == 2) or (ops == 5):
            if a > b:
                self.problem["result"] = a - b
            else:
                self.problem["num1"] = b
                self.problem["num2"] = a
                self.problem["result"] = b - a
            self.operation = "subtraction"

        else:
            a = random.randint(0,20)
            b = random.randint(0,20)
            self.problem["num1"] = a
            self.problem["num2"] = b
            self.problem["result"] = a * b
            self.operation = "multiplication"


    def hard_level(self):
        #Se define las operaciones de suma, resta, multiplicación y división
        #Establece num1,num2 y el resultado para el nivel 3
        ops = random.randint(1,8)
        a = random.randint(0,100)
        b = random.randint(0,100)

        self.problem["num1"] = a
        self.problem["num2"] = b

        if (ops == 1) or (ops == 5):
            self.problem["result"] = a + b
            self.operation = "addition"

        elif (ops == 2) or (ops == 6):
            if a > b:
                self.problem["result"] = a - b
            else:
                self.problem["num1"] = b
                self.problem["num2"] = a
                self.problem["result"] = b - a
            self.operation = "subtraction"

        elif (ops == 3) or (ops == 7):
            a = random.randint(0,20)
            b = random.randint(0,10)
            self.problem["num1"] = a
            self.problem["num2"] = b
            self.problem["result"] = a * b
            self.operation = "multiplication"

        else:
            divisor = random.randint(1,12)
            dividend = divisor * random.randint(1,12)
            q = dividend / divisor
            self.problem["num1"] = dividend
            self.problem["num2"] = divisor
            self.problem["result"] = round(q)
            self.operation = "division"


    def check_result(self):
        #Se revisa el resultado que escoge el jugador 
        for button in self.button_list:
            if button.isPressed():
                if button.get_number() == self.problem["result"]:
                    # Establecer color verde cuando se escoje la respuesta correcta
                    button.set_color(GREEN)
                    # Incrementar el puntaje a 5
                    self.score += 5
                    # Baja vida de Covid 10
                    if self.life <= 200:
                        self.life -= 10
                    # Reproduce el efecto de sonido de un spray cuando es correcto
                    self.sound_1.play()
                else:
                    # Establecer color rojo cuando se escoje la respuesta incorrecta
                    button.set_color(RED)
                    # Aumenta la vida del covid 5
                    self.life += 5
                    # Reproducir sonido2 de tos (hacer referencia al covid) cuando es incorrecto
                    self.sound_2.play()
                # Establecer reset_problem True para que pase al siguente problema
                self.reset_problem = True


    def set_problem(self):
        #Hace otro problema nuevo y dependiendo del nivel que elijas 
        #te abre los problemas con sus operaciones correspondientes
        if self.level == 1:
            self.easy_level()
        elif self.level == 2:
            self.medium_level()
        elif self.level == 3:
            self.hard_level()
        self.button_list = self.get_button_list()
        

    def process_events(self,screen):
        for event in pygame.event.get():  # El jugador hizo algo
            if event.type == pygame.QUIT: # Si el juagdor oprime cerrar
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_menu:
                    if self.menu.state == 0:
                        self.level = 1
                        self.set_problem()
                        #Se comienza en 10 para que solo se hagan 10 preguntas en nivel 1
                        self.count = 10
                        self.life = 100
                        self.show_menu = False
                    elif self.menu.state == 1:
                        self.level = 2
                        self.set_problem()
                        #Se comienza en 8 para que solo se hagan 12 preguntas en nivel 2
                        self.count = 8
                        self.life = 120
                        self.show_menu = False
                    elif self.menu.state == 2:
                        self.level = 3
                        self.set_problem()
                        self.life = 200
                        self.show_menu = False
                    elif self.menu.state == 3:
                        screen.blit(self.background_image,(0,0))
                        msg = "Presentado por:"
                        msg1 = "Camila, Mariana y Laura"
                        self.display_message(screen,(msg,msg1))
                        pygame.display.flip()
                        pygame.time.wait(6000)
                        self.show_menu = True

                # Se va a la funcioón: check_result para revisar si el jugador respondió correctamente
                else:
                    self.check_result()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu = True
                    # resetear 
                    self.score = 0
                    self.life = 100
                    self.count = 0
        return False


    def run_logic(self):
        # Actualizar 
        self.menu.update()


    def display_message(self,screen,items):
        #Muestra cada cadena que esta dentro de la tupla.
        for index, message in enumerate(items):
            label = self.font_1.render(message,True,BLACK)
            # Obtener el ancho y alto de la etiqueta que se utiliza para mostrar el texto
            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: altura total del bloque de texto
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)

            screen.blit(label,(posX,posY))


    def display_frame(self,screen):
        # Dibujar la imagen de fondo
        screen.blit(self.background_image,(0,0))
        # True: se llama a pygame.time.wait()
        time_wait = False
        # El codigo para dibujar
        if self.show_menu:
            self.menu.display_frame(screen)
        elif self.count == 20:
            # Si self.count llega a 20 significa que se acaba el nivel y el juego
            # Se muestra cuantas respuestas fueron correctas y si vences o no al covid 
            # dependiendo de cuanta vida le bajaste.
            msg_1 = "Respondiste " + str(round(self.score / 5)) + " correctamente"
            if self.life <= 40:
                msg_2 = "Victoria! venciste al Covid"
                self.display_message(screen,(msg_1,msg_2))
            else:
                msg_3 = "Game Over :c, la proxima lo vences!"
                self.display_message(screen,(msg_1,msg_3))
            self.show_menu = True
            # Restablecer el puntaje, la vida del covid y en contador para las preguntas
            self.score = 0
            self.life = 100
            self.count = 0
            # Establecer time_wait True para esperar 3 segundos
            time_wait = True
        else:
            # Crear etiquetas que se utilizan las para mostrar cada número
            label_1 = self.font.render(str(self.problem["num1"]),True,BLACK)
            label_2 = self.font.render(str(self.problem["num2"])+" = ?",True,BLACK)
            # t_w: ancho total y 64 es la longitud del símbolo
            t_w = label_1.get_width() + label_2.get_width() + 64 
            posX = (SCREEN_WIDTH / 2) - (t_w / 2)
            screen.blit(label_1,(posX,130))
            # Imprimir el símbolo en la pantalla
            screen.blit(self.symbols[self.operation],(posX + label_1.get_width(),120))
            screen.blit(label_2,(posX + label_1.get_width() + 64,130))
            # Pasar por cada boton y dibujarlo
            for btn in self.button_list:
                btn.draw(screen)
            # Mostrar el score y la vida del covid, en cada posición
            score_label = self.score_font.render("Score: "+str(self.score),True,BLACK)
            screen.blit(score_label,(10,320))
            life_label = self.life_font.render("Covid: "+str(self.life),True,BLACK)
            screen.blit(life_label,(470,320))

        #Actualizar la pantalla con lo que se a dibujado
        pygame.display.flip()
        #Esto es para que el juego espere unos segundos antes de
        #mostrar lo que se dibujó antes de cambiar de cuadro
        if self.reset_problem:
            # Esperar 2 segundos por cada pregunta
            pygame.time.wait(2000)
            self.set_problem()
            # Aumentar count por 1 cuando se pasa de una pregunta a otra
            self.count += 1
            self.reset_problem = False
        elif time_wait:
            # Esperar 8 segundos cuando se muestra los mensajes del final al terminar el juego 
            pygame.time.wait(8000)



class Button(object):
    def __init__(self,x,y,width,height,number):
        self.rect = pygame.Rect(x,y,100,70)
        self.font = pygame.font.Font(None,40)
        self.text = self.font.render(str(number),True,BLACK)
        self.number = number
        self.background_color = WHITE


    def draw(self,screen):
        # Primero se llena la pantalla con el color de fondo
        pygame.draw.rect(screen,self.background_color,self.rect)
        # Dibujar los bordes del boton y su anchura que es 2
        pygame.draw.rect(screen,BLACK,self.rect,2)
        # Obtener el ancho y la altura de la superficie del texto
        width = self.text.get_width()
        height = self.text.get_height()
        # Calcular las posiciones
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        # Dibujar la imagen en la pantalla
        screen.blit(self.text,(posX,posY))


    def isPressed(self):
        #Para obtener la posición, retornar verdadero si el punto que se oprime 
        #con el mouse esta dentro de los recuadros (rectangulos Rect)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False


    def set_color(self,color):
        self.background_color = color


    def get_number(self):
        return self.number


