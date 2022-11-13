# Yeety

Yeelight (Xiaomi Mi Light) RGB ambience controller for GNU/Linux. Works by taking a screenshot (of a specified monitor) 2-3 times per second, and setting the light bulb's color to the dominant color on the screenshot. You can enable rate limiting so that your client does not get blocked.

## Status

**STABLE, NO SOLID FUTURE** - You can use it I guess.

## Features

- 🖥 **Single** monitor support
- 💡 **Single** RGB bulb support
- 🐌 Blazing *slow* response time
- It works tho :D

## Requirements

- Python 3+
- git
- pip
- os
- mss (for screenshots)
- time
- yeelight
- colorthief
- Dev mode/LAN control enabled for the light bulb

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/recoskyler/yeety.git; cd yeety; chmod +x yeety.py
    ```

2. Install the required packages:

    ```bash
    pip3 install -U mss colorthief yeelight
    ```

3. Set the necessary vars in the [yeety.py](yeety.py) file:

    ```bash
    nano ./yeety.py
    ```

    ```py
    # ./yeety.py

    # ...

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
    light_ip = "192.168.1.23"

    ##* REQUIRED-ish ("sudden"/"smooth", can be None, will default to "smooth")
    effect = "smooth"

    ##* REQUIRED-ish (can be None, will default to False)
    auto_on = True

    ##* REQUIRED-ish (min 30, can be None, will default to 300ms)
    duration = 300

    #*#############################################################################

    # ...
    ```

4. Run the file using the command:

    ```bash
    ./yeety.py
    ```

    **or run it in the background using:**

    ```bash
    nohup ./yeety.py &
    ```

    `nohup COMMAND &` *allows the command to detach and run in the background, so that you can close the terminal.*

## [License](LICENSE)
