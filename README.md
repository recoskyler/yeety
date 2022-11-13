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
- pip
- git
- mss (for screenshots)
- yeelight
- os
- time
- colorsys
- math
- colorthief
- Dev mode/LAN control enabled for the light bulb

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/recoskyler/yeety.git; cd yeety; chmod +x yeety.py
    ```

2. Set the necessary vars in the [yeety.py](yeety.py) file.
3. Run the file using the command:

    ```bash
    ./yeety.py
    ```

    **or run it in the background using:**

    ```bash
    nohup ./yeety.py &
    ```

    `nohup COMMAND &` *allows the command to detach and run in the background, so that you can close the terminal.*

## [License](LICENSE)
