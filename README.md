# Yeety

Yeelight (Xiaomi Mi Light) RGB ambience controller for GNU/Linux. Works by taking a screenshot (of a specified monitor) 2-3 times per second, and setting the light bulb's color to the dominant color on the screenshot. You can enable rate limiting so that your client does not get blocked.

## Status

**STABLE, NO SOLID FUTURE** - You can use it I guess.

## Features

- 🖥 **Single Monitor** support
- 💡 **Single RGB Bulb** support
- 🐌 **Blazing *Slow*** response time
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

## Setup & Usage

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

    #*###########################
    #* SET UP THE VARIABLES BELOW
    #*###########################

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

    #*###########################

    # ...
    ```

4. Run the file using the command:

    ```bash
    ./yeety.py
    ```

    Press <kbd>Ctrl</kbd>+<kbd>c</kbd> to stop the program

## Running in the background

```bash
nohup ./yeety.py &
```

`nohup COMMAND &` *allows the command to detach and run in the background, so that you can close the terminal.*

### Stopping the background app

1. Type the following command in the terminal:

    ```bash
    ❯ ps -x | grep yeety.py
    ```

2. Take a look at the command's output. If you see a line similar to `350017 ?        RN     4:47 /usr/bin/python3 ./yeety/yeety.py`. If you don't see a line similar to this one, then the background app is not running. The following is an example of a full output:

    ```bash
    350017 ?        RN     4:47 /usr/bin/python3 ./yeety/yeety.py
    352201 pts/1    S+     0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox yeety.py
    ```

    You should ignore the part with `grep --color=auto .....`

    The thing we are interested in is the first number on the interesting line: `350017`, which will be different in your case. Copy that number to your clipboard.

3. Type the following command to exterminate the background app:

    ```bash
    kill 350017
    kill THE_NUMBER_YOU_JUST_COPIED
    ```

## [License](LICENSE)
