# 4 лаба
import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


# 4.1
def shader_41(x, y):
    inside = max(abs(x - 0.5), abs(y - 0.5)) <= 0.4
    c = 1 - inside
    return c, c, c


# 4.2
def shader_42(x, y):
    dx = (x - 0.48) / 0.37
    dy = (y - 0.48) / 0.37
    z = math.sqrt(max(0, 1 - dx * dx - dy * dy))
    u = (dx + dy) / 2
    return z * (1 + 2 * u), z * (1 - 2 * u), 0


# 4.3
def shader_43(x, y):
    dx = x - 0.5
    dy = y - 0.5
    disk = dx * dx + dy * dy <= 0.3125 ** 2
    mouth = abs(dy) <= dx * math.tan(math.pi / 6)
    eye = (x - 0.6) ** 2 + (y - 0.3) ** 2 <= 0.055 ** 2
    c = disk * (1 - mouth) * (1 - eye)
    return c, c, 0


# 4.4
def noise(x, y):
    return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1


def shader_44(x, y):
    n = noise(x, y)
    return n, n, n


# Раскомментируй ту задачу, которую хочешь запустить:
# main(shader_41)
# main(shader_42)
# main(shader_43)
main(shader_44)