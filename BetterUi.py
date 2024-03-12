"""
$$$$$$$\             $$\     $$\                         $$\   $$\ $$\  $$$$\  
$$  __$$\            $$ |    $$ |                        $$ |  $$ |\__|$$  $$\ 
$$ |  $$ | $$$$$$\ $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$ |  $$ |$$\ \__/$$ |
$$$$$$$\ |$$  __$$\\_$$  _|\_$$  _|  $$  __$$\ $$  __$$\ $$ |  $$ |$$ |   $$  |
$$  __$$\ $$$$$$$$ | $$ |    $$ |    $$$$$$$$ |$$ |  \__|$$ |  $$ |$$ |  $$  / 
$$ |  $$ |$$   ____| $$ |$$\ $$ |$$\ $$   ____|$$ |      $$ |  $$ |$$ |  \__/  
$$$$$$$  |\$$$$$$$\  \$$$$  |\$$$$  |\$$$$$$$\ $$ |      \$$$$$$  |$$ |  $$\   
\_______/  \_______|  \____/  \____/  \_______|\__|       \______/ \__|  \__|  
by seka <3
"""

import time
import datetime
from os import system as sysc, name, get_terminal_size as term_size

WINDOWS = name == "nt"

class Color:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREY = "\033[90m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_PURPLE = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    RESET = "\033[0m"

    def __str__(self):
        sysc("")

class Terminal:
    @staticmethod
    def clear():
        sysc("cls" if WINDOWS else "clear")

    @staticmethod
    def title(title: str):
        sysc(f"title {title}" if WINDOWS else "echo Title Error.")

class Display:
    @staticmethod
    def print(thing: any, content: any, _input: bool = False, new_line: bool = True) -> str:
        part = f"{Color.BRIGHT_CYAN}[{thing}]{Color.RESET} | {Color.BRIGHT_YELLOW}{content}{Color.RESET}"

        if _input:
            return f"{part}{Color.RESET}"
        if not new_line:
            print(f"{part}{Color.RESET}", end="\r")
        else:
            print(f"{part}{Color.RESET}")

    @staticmethod
    def timer(timee, title: str = "Sleep"):
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(seconds=timee)

        while datetime.datetime.now() < end_time:
            remaining_time = (end_time - datetime.datetime.now()).total_seconds()
            remaining_time_2 = round(remaining_time, 2)

            Display.print(title, f"Remaining Time: {Color.RESET}{remaining_time_2}", new_line = False)
            time.sleep(0.1)

    @staticmethod
    def typing(text: str, interval: bool = 0.05):
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(interval)
        return ""

class Center:
    @staticmethod
    def center(text):
        return Center.center_x(Center.center_y(text))

    @staticmethod
    def center_x(text):
        terminal_width = term_size().columns
        return "\n".join(line.center(terminal_width) for line in text.splitlines())
    
    @staticmethod
    def center_y(text):
        terminal_height = term_size().lines
        lines = text.splitlines()
        num_lines = len(lines)
        if num_lines >= terminal_height:
            return text
        top_padding = (terminal_height - num_lines) // 2
        bottom_padding = terminal_height - num_lines - top_padding
        return "\n".join(" " * term_size().lines for _ in range(top_padding)) + text + "\n".join(" " * term_size().lines for _ in range(bottom_padding))