import pyautogui as pg
import keyboard as kb
import time as t
import math as m

X, Y = 842, 527
ColorThreshold = 30

initial_color = pg.pixel(X, Y)

def calculate_color_difference(color1, color2):
    return m.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

while True:
    screen = pg.screenshot()
    current_color = screen.getpixel((X, Y))

    if kb.is_pressed("t"):
        print("F2 Clicked")
        initial_color = pg.pixel(X, Y)

        color_difference = calculate_color_difference(initial_color, current_color)

        if color_difference >= ColorThreshold:
            print(f"Color difference is {round(color_difference)}. Clicking.")
            t.sleep(0.01)
            pg.click()
