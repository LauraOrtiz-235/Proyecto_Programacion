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
        self.font_1 = pygame.font.Font("Triforce.TTF",40)
        # Crear la fuente para el mensaje de la puntuación final
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
        # Crear un booleano que es 'true' cuando se hace click con el mouse
        self.reset_problem = False
        # Crear menu
        items = ("Easy","Medium","Hard")
        self.menu = Menu(items,ttf_font="Fonts_items.TTF",font_size=50)
        # True: muestra menu
        self.show_menu = True
        # Crear el contador del puntaje
        self.score = 0
        # Crear el contador de vida del covid
        self.life = 100
        # Contar el número de problemasCount the number of problems
        self.count = 0
        # Cargar la imagen de fondo
        self.background_image = pygame.image.load("fondo_game.jpg").convert()
        # Cargar los efectos de sonido
        self.sound_1 = pygame.mixer.Sound("item1.ogg")
        self.sound_2 = pygame.mixer.Sound("item2.ogg")
        # Crear la variable donde depende el nivel 
        self.level = 0

    def get_button_list(self):
        """ Return a list with four buttons """
        button_list = []
        # Asignar uno de los botones como la respuesta correcta
        choice = random.randint(1,4)
        # Definir el ancho y el alto de los botones
        width = 100
        height = 100
        # t_w: ancho total
        t_w = width * 2 + 50
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


    def get_symbols(self):
        """ Return a dictionary with all the operation symbols """
        symbols = {}
        sprite_sheet = pygame.image.load("symbols.png").convert()
        image = self.get_image(sprite_sheet,0,0,64,64)
        symbols["addition"] = image
        image = self.get_image(sprite_sheet,64,0,64,64)
        symbols["subtraction"] = image
        image = self.get_image(sprite_sheet,128,0,64,64)
        symbols["multiplication"] = image
        image = self.get_image(sprite_sheet,192,0,64,64)
        symbols["division"] = image

        return symbols

    def get_image(self,sprite_sheet,x,y,width,height):
        """ This method will cut an image and return it """
        # Crear una imagen en blanco
        image = pygame.Surface([width,height]).convert()
        # Copiar el sprite de un hoja mñas grande a una más pequeña
        image.blit(sprite_sheet,(0,0),(x,y,width,height))
        # Retornar la imagen
        return image


    def easy_level(self):
        """ These will set num1,num2,result for addition """
        ops = random.randint(1,2)
        a = random.randint(0,100)
        b = random.randint(0,100)
        print(ops)

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
        """ These will set num1,num2,result for subtraction """
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
        """ These will set num1,num2,result for multiplication """
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
        """ Check the result """
        for button in self.button_list:
            if button.isPressed():
                if button.get_number() == self.problem["result"]:
                    # Establecer color verde cuando se escoje la respuesta correcta
                    button.set_color(GREEN)
                    # Incrementar el puntaje
                    self.score += 5
                    # Baja vida de Covid
                    self.life -= 10
                    # Reproducir efecto de sonido
                    self.sound_1.play()
                else:
                    # Establecer color rojo cuando se escoje la respuesta incorrecta
                    button.set_color(RED)
                    # Aumenta la vida del covid
                    self.life += 5
                    # Reproducir efecto de sonido2
                    self.sound_2.play()
                # Establecer reset_problem True para que pase al siguente problema
                # Se usa reset_problem en display_frame para esperar un segundo
                self.reset_problem = True


    def set_problem(self):
        """ hacer otro problema nuevamente """
        if self.level == 1:
            self.easy_level()

        elif self.level == 2:
            self.medium_level()

        elif self.level == 3:
            self.hard_level()
        self.button_list = self.get_button_list()


    def process_events(self):
        for event in pygame.event.get():  # El jugador hizo algo
            if event.type == pygame.QUIT: # Si el juagdor oprimió cerrar
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_menu:
                    if self.menu.state == 0:
                        self.level = 1
                        self.set_problem()
                        #Se comienza en 12 para que solo se hagan 8 preguntas en nivel 1
                        self.count = 12
                        self.show_menu = False
                    elif self.menu.state == 1:
                        self.level = 2
                        self.set_problem()
                        #Se comienza en 8 para que solo se hagan 12 preguntas en nivel 2
                        self.count = 8
                        self.show_menu = False
                    elif self.menu.state == 2:
                        self.level = 3
                        self.set_problem()
                        self.show_menu = False

                # Se va a la funcioón: check_result para revisar
                # si el jugador respondió correctamente
                else:
                    self.check_result()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu = True
                    # set score to 0
                    self.score = 0
                    self.life = 100
                    self.count = 0

        return False

    def run_logic(self):
        # Actualizar menu
        self.menu.update()


    def display_message(self,screen,items):
        """ mostrar cada cadena que esta dentro de la tupla(args) """
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
        # --- El codigo para dibujar
        if self.show_menu:
            self.menu.display_frame(screen)
        elif self.count == 20:
            # Si self.count llega a 20 significa que se acaba el nivel y el juego
            # Se muestra cuantas respuestas fueron correctas y el puntaje

            msg_1 = "Tu respondiste " + str(round(self.score / 5)) + " correctamente"
            if self.life <= 40:
                msg_2 = "Victoria! venciste al Covid"
                self.display_message(screen,(msg_1,msg_2))
            else:
                msg_3 = "Animo.. la proxima lo vences!"
                self.display_message(screen,(msg_1,msg_3))
            self.show_menu = True
            # Restablecer el puntaje y self.cout a 0
            self.score = 0
            self.life = 100
            self.count = 0
            # Establecer time_wait True para esperar 3 segundos
            time_wait = True
        else:
            # Crear etiquetas que se utilizan las para mostrar cada número
            label_1 = self.font.render(str(self.problem["num1"]),True,BLACK)
            label_2 = self.font.render(str(self.problem["num2"])+" = ?",True,BLACK)
            # t_w: ancho total
            t_w = label_1.get_width() + label_2.get_width() + 64 # 64: longitud del símbolo
            posX = (SCREEN_WIDTH / 2) - (t_w / 2)
            screen.blit(label_1,(posX,130))
            # Imprimir el símbolo en l pantalla
            screen.blit(self.symbols[self.operation],(posX + label_1.get_width(),120))
            screen.blit(label_2,(posX + label_1.get_width() + 64,130))
            # Pasar por cada boton y dibujarlo
            for btn in self.button_list:
                btn.draw(screen)
            # Mostrar la puntuación
            score_label = self.score_font.render("Score: "+str(self.score),True,BLACK)
            screen.blit(score_label,(10,320))
            life_label = self.life_font.render("Covid: "+str(self.life),True,BLACK)
            screen.blit(life_label,(480,320))

        # --- Actualizar la pantalla con lo que se a dibujado
        pygame.display.flip()
        # --- Esto es para que el juego espere unos segundos antes de
        # --- mostrar lo que se dibujó andtes de cambiar de cuadro
        if self.reset_problem:
            # Esperar 1 segundo
            pygame.time.wait(1000)
            self.set_problem()
            # Aumentar count por 1
            self.count += 1
            self.reset_problem = False
        elif time_wait:
            # Esperar tres segundos
            pygame.time.wait(10000)


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
        # Dibujar los bordes del boton
        pygame.draw.rect(screen,BLACK,self.rect,2)
        # Obtener el ancho y la altura de la superficie del texto
        width = self.text.get_width()
        height = self.text.get_height()
        # Calcular posX and posY
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        # Dibujar la imagen en la pantalla
        screen.blit(self.text,(posX,posY))


    def isPressed(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False


    def set_color(self,color):
        self.background_color = color


    def get_number(self):
        return self.number
