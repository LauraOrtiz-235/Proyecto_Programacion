import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Menu(object):
    state = -1
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        # Se genera la lista que contiene los recuadros de cada item.
        self.rect_list = self.get_rect_list(items)


    def get_rect_list(self,items):
        rect_list = []
        for index, item in enumerate(items):
            # Se determina la cantidad de espacio necesario para presentar texto.
            size = self.font.size(item)
            # Obtiene el ancho y alto del texto.
            width = size[0]
            height = size[1]

            posX = (SCREEN_WIDTH / 2) - (width /2)
            # t_h: altura total del bloque de texto
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            # Se crean los recuadros (Rect-rectángulos)
            rect = pygame.Rect(posX,posY,width,height)
            # Se agregan los recuadros a la lista
            rect_list.append(rect)

        return rect_list


    #Collide_points guarda donde se encuentra el mouse
    #si esta dentro de los recuadros (Rect-rectángulos)
    def collide_points(self):
        index = -1
        mouse_pos = pygame.mouse.get_pos()
        for i,rect in enumerate(self.rect_list):
            if rect.collidepoint(mouse_pos):
                index = i

        return index


    def update(self):
        # Se asignan los collide_points al estado (self.state)
        self.state = self.collide_points()


    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)

            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: altura total del bloque de texto
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)

            screen.blit(label,(posX,posY))
