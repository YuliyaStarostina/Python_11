"""Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод."""
# import time


# class TrafficLight:
# #     __color_red = "Red"
# #     __color_yellow = "Yellow"
# #     __color_green = "Green"

# #     def running(self):
# #         while(True):
# #             print("\033[31m {}".format(self.__color_red))
# #             time.sleep(7)
# #             print("\033[33m {}".format(self.__color_yellow))
# #             time.sleep(2)
# #             print("\033[32m {}".format(self.__color_green))
# #             time.sleep(7)


# # a = TrafficLight()
# # a.running()
# # ____________________________________________________________

# """Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т."""

class Road():

    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def calculation(self):
        print(f"При ширине дороги {self._width} м и длинне {self._length} м понадобится "
              + str(self._length * self._width * 25 * 5)[:5] + " тонн асфальта")

a = Road(5000, 20)
a.calculation()

#____________________________________________________________

"""Крестики нолики"""


# import sys
# import pygame

# def check_win(mas, sign):
#     zeros = 0
#     for row in mas:
#         zeros += row.count(0)
#         if row.count(sign) == 3:
#             return sign
#     for col in range(3):
#         if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
#             return sign
#     if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
#         return sign
#     if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
#         return sign
#     if zeros == 0:
#         return 'Peace'
#     return False


# pygame.init()
# block_size = 100
# margin = 15
# width = height = block_size * 3 + margin * 4
# size = (width, height)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('Крестики нолики')
# img = pygame.image.load('icon.png')
# pygame.display.set_icon(img)
# black = (0, 0, 0)
# white = (255, 255, 255)
# green = (0, 255, 0)
# red = (255, 0, 0)
# mas = [[0]*3 for i in range(3)]
# query = 0

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit(0)
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             x_mouse, y_mouse = pygame.mouse.get_pos()
#             col = x_mouse // (block_size + margin)
#             row = y_mouse // (block_size + margin)
#             if mas[row][col] == 0:
#                 if query%2 == 0:
#                     mas[row][col] = 'X'
#                 else:
#                     mas[row][col] = 'O'
#                 query += 1

#     for row in range(3):
#         for col in range(3):
#             if mas[row][col] == 'X':
#                 color = red
#             elif mas[row][col] == 'O':
#                 color = green
#             else:
#                 color = white
#             x = col * block_size + (col + 1) * margin
#             y = row * block_size + (row + 1) * margin
#             pygame.draw.rect(screen, color, (x, y, block_size, block_size))
#             if color == red:
#                 pygame.draw.line(screen, white, (x+ 5, y + 5), (x + block_size - 5, y + block_size - 5), 3)
#                 pygame.draw.line(screen, white, (x + block_size - 5, y + 5), (x + 5, y + block_size - 5), 3)
#             elif color == green:
#                 pygame.draw.circle(screen, white, (x + block_size // 2, y + block_size // 2), block_size // 2 - 3, 3)
#     if (query - 1) % 2 == 0:
#         game_over = check_win(mas, 'X')
#     else:
#         game_over = check_win(mas, 'O')

#     if game_over:
#         screen.fill(black)
#         font = pygame.font.SysFont('stxingkai', 80)
#         text1 = font.render(game_over, True, white)
#         text_rect = text1.get_rect()
#         text_x = screen.get_width() / 2 - text_rect.width / 2
#         text_y = screen.get_height() / 2 - text_rect.height / 2
#         screen.blit(text1, (text_x, text_y))
#     pygame.display.update()
