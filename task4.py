# 4 лаба: пиксельные шейдеры
import math
import tkinter as tk


def draw(shader, width, height):
    # Буфер изображения: по 3 байта (R, G, B) на каждый пиксель
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            # Позиция пикселя в буфере
            pos = (width * y + x) * 3
            # Вызываем шейдер, передавая координаты в диапазоне [0, 1)
            color = shader(x / width, y / height)
            # Переводим компоненты цвета из [0, 1] в [0, 255] и обрезаем лишнее
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    # Заголовок формата PPM (P6), который понимает tkinter
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    # Рисуем картинку 256x256 и увеличиваем в 2 раза (получается 512x512)
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


# 4.1 Чёрный квадрат
def shader_41(x, y):
    # Расстояние до центра по "максимальной" норме: даёт квадрат
    # Внутри квадрата со стороной 0.8 условие истинно (True = 1)
    inside = max(abs(x - 0.5), abs(y - 0.5)) <= 0.4
    c = 1 - inside  # внутри 0 (чёрный), снаружи 1 (белый)
    return c, c, c


# 4.2 Шар
def shader_42(x, y):
    # Смещаем центр и нормируем координаты на радиус шара
    dx = (x - 0.48) / 0.37
    dy = (y - 0.48) / 0.37
    # "Высота" точки на сфере: в центре 1, к краю падает до 0 (затемнение)
    z = math.sqrt(max(0, 1 - dx * dx - dy * dy))
    # Диагональный сдвиг: определяет, где зелёный, а где красный
    u = (dx + dy) / 2
    # Красный растёт в одну сторону, зелёный в другую, в центре получается жёлтый
    return z * (1 + 2 * u), z * (1 - 2 * u), 0


# 4.3 Pac-Man
def shader_43(x, y):
    dx = x - 0.5
    dy = y - 0.5
    # Круг радиусом 0.3125
    disk = dx * dx + dy * dy <= 0.3125 ** 2
    # Рот: клин с вершиной в центре, полуугол 30 градусов
    mouth = abs(dy) <= dx * math.tan(math.pi / 6)
    # Глаз: маленький круг
    eye = (x - 0.6) ** 2 + (y - 0.3) ** 2 <= 0.055 ** 2
    # Круг без рта и без глаза
    c = disk * (1 - mouth) * (1 - eye)
    return c, c, 0  # R = G = c даёт жёлтый цвет


# 4.4 Шум
def noise(x, y):
    # Хэш на основе синуса: одинаковые координаты всегда дают одинаковое
    # "случайное" число. % 1 оставляет только дробную часть, то есть [0, 1)
    return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1


def shader_44(x, y):
    n = noise(x, y)
    return n, n, n  # серый шум


# 4.5 Интерполяционный шум (value noise)
def val_noise(x, y):
    # Целая часть: номер ячейки сетки, дробная: положение внутри ячейки
    ix = math.floor(x)
    iy = math.floor(y)
    fx = x - ix
    fy = y - iy

    # Сглаживание (smoothstep): убирает резкие переходы на границах ячеек
    sx = fx * fx * (3 - 2 * fx)
    sy = fy * fy * (3 - 2 * fy)

    # Случайные значения в четырёх углах ячейки
    a = noise(ix, iy)          # левый верхний
    b = noise(ix + 1, iy)      # правый верхний
    c = noise(ix, iy + 1)      # левый нижний
    d = noise(ix + 1, iy + 1)  # правый нижний

    # Линейная интерполяция по x сверху и снизу, затем по y между ними
    top = a + (b - a) * sx
    bottom = c + (d - c) * sx
    return top + (bottom - top) * sy


def shader_45(x, y):
    # 32 ячейки по ширине: меньше число даёт крупнее пятна, больше мельче
    n = val_noise(x * 32, y * 32)
    return n, n, n


# Раскомментируй ровно одну строку, которую хочешь запустить:
# main(shader_41)
# main(shader_42)
# main(shader_43)
# main(shader_44)
main(shader_45)