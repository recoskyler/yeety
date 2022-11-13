#!/usr/bin/python3

import yeelight as yl
import os
import time
import colorsys as cs
import math
from colorthief import ColorThief


#*################################################################################################################################
#* SET UP THE VARIABLES BELOW
#*################################################################################################################################

screenshot_path = "/tmp/yeet/monitor.png" ##! REQUIRED
monitor = 2                               ##! REQUIRED (min 0)
max_per_second = 55                       ##! REQUIRED (min 1)
light_ip = "192.168.1.41"                 ##? Optional
effect = "smooth"                         ##* REQUIRED-ish ("sudden"/"smooth", can be None, will default to "smooth")
auto_on = True                            ##* REQUIRED-ish (can be None, will default to False)
duration = 250                            ##* REQUIRED-ish (min 30, can be None, will default to 300ms)

#*################################################################################################################################


prev_dominatrix_color = (0, 0, 0)         ##! DO NOT CHANGE
last_refresh = 0                          ##! DO NOT CHANGE


def colorfulness(color):
    """
    It converts the RGB color to HSV, then returns the square root of the sum of the squares of the
    saturation and value components

    :param color: The color to be analyzed
    :return: The colorfulness of the color.
    """
    h, s, v = cs.rgb_to_hsv(color[0], color[1], color[2])

    return math.sqrt(pow(s, 2) + pow(v, 2))


def refresh(bulb):
    """
    It takes a screenshot of the screen, finds the dominant color, and sets the bulb to that color

    :param bulb: the bulb object
    """
    global prev_dominatrix_color
    global last_refresh
    global screenshot_path

    os.system(f"mss -o {screenshot_path} -m {monitor} -q")

    color_thief = ColorThief(screenshot_path)
    dominatrix_color = color_thief.get_color()

    if dominatrix_color != prev_dominatrix_color:
        print("refreshing...")

        en = time.time()
        sl = (60 / max_per_second) - (en - last_refresh)

        if sl > 0:
            time.sleep(sl)

        bulb.set_rgb(int(dominatrix_color[0]), int(dominatrix_color[1]), int(dominatrix_color[2]))

        prev_dominatrix_color = dominatrix_color


def main():
    """
    `main()` is a function that finds the IP address of the light bulb, and then calls `refresh()` every
    second
    """
    global light_ip

    if light_ip == None:
        bulbs = yl.discover_bulbs()

        if len(bulbs) == 0 and light_ip == None:
            exit("No bulbs found");

        light_ip = bulbs[0]["ip"]

    print(f"Light IP: {light_ip}")

    bulb = yl.Bulb(light_ip, effect=effect, auto_on=auto_on, duration=duration)

    while True:
        refresh(bulb)


if __name__ == "__main__":
    print("Checking for screenshot folder...")
    dirname = os.path.dirname(screenshot_path)

    if not os.path.exists(dirname):
        print("Creating screenshot folder...")
        os.mkdir(dirname)
        print("Created screenshot folder")

    main()