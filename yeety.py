#!/usr/bin/python3

import os
import time
import signal
import readchar
import yeelight as yl
from colorthief import ColorThief


#*#############################################################################
#* SET UP THE VARIABLES BELOW
#*#############################################################################

##! REQUIRED
screenshot_path = "/tmp/yeety/screenshot.png"

##! REQUIRED (min 0)
monitor = 2

##! REQUIRED (min 1)
max_per_second = 55

##! REQUIRED (min 1, max 10. 1 Highest quality, takes the longest time...)
quality = 10

##? Optional
light_ip = "192.168.1.41"

##* REQUIRED-ish ("sudden"/"smooth", can be None, will default to "smooth")
effect = "smooth"

##* REQUIRED-ish (can be None, will default to False)
auto_on = True

##* REQUIRED-ish (min 30, can be None, will default to 300ms)
duration = 500

#*#############################################################################


prev_dominatrix_color = (0, 0, 0)         ##! DO NOT CHANGE
last_refresh = 0                          ##! DO NOT CHANGE
running = False                           ##! DO NOT CHANGE

# Thanks to Gabor Szabo
# https://code-maven.com/catch-control-c-in-python

def handler(signum, frame):
    global running

    msg = "\n\nCtrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)

    res = readchar.readchar()

    if res == 'y':
        running = False
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)


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
    dominatrix_color = color_thief.get_color(quality=quality)

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
    global running

    try:
        if light_ip == None:
            bulbs = yl.discover_bulbs()

            if len(bulbs) == 0 and light_ip == None:
                exit("No bulbs found");

            light_ip = bulbs[0]["ip"]

        print(f"Light IP: {light_ip}")

        bulb = yl.Bulb(light_ip, effect=effect, auto_on=auto_on, duration=duration)

        running = True

        while running:
            try:
                refresh(bulb)
            except:
                print("An exception occurred while refreshing")
    except:
        print('An exception occurred')


if __name__ == "__main__":
    print("Checking for screenshot folder...")
    dirname = os.path.dirname(screenshot_path)

    signal.signal(signal.SIGINT, handler)

    try:
        if not os.path.exists(dirname):
            print("Creating screenshot folder...")
            os.mkdir(dirname)
            print("Created screenshot folder")

        main()
    except:
        print("Failed to check for/create temp screenshot folder")