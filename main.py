import sys
import gptclientai
from BetterUi import *

messages = []

banner = f"""{Color.BRIGHT_PURPLE}
 _____ _                      
/  ___| |                     
\ `--.| | ___   _ _ __   __ _ 
 `--. \ |/ / | | | '_ \ / _` |
/\__/ /   <| |_| | | | | (_| |
\____/|_|\_\\\__,_|_| |_|\__,_|
{Color.RESET}
"""

def setup_gui():
    Terminal.clear()
    Terminal.title("Skuna")

    messages = []

    print(Center.center_x(banner))
    Display.print("-", "Welcome to SkunaGPT")
    Display.print("-", f"Say '{Color.BRIGHT_RED}exit{Color.BRIGHT_YELLOW}' if you want to {Color.BRIGHT_RED}leave{Color.BRIGHT_YELLOW}.")
    Display.print("-", f"And '{Color.BRIGHT_BLUE}retry{Color.BRIGHT_YELLOW}' if you want to get another {Color.BRIGHT_BLUE}chance{Color.BRIGHT_YELLOW}.")
    Display.print("-", f"Ask me {Color.BRIGHT_GREEN}something{Color.BRIGHT_YELLOW} and i will {Color.BRIGHT_GREEN}answer{Color.BRIGHT_YELLOW}.")
    print("")
    
if __name__ == "__main__":
    setup_gui()

    while True:
        you = input(Display.print("You", f"> {Color.RESET}", True))
        print("")

        messages.append({
            "role": "user",
            "content": you
        })

        res = gptclientai.Chat.create_chat_response(
            provider = gptclientai.Provider.DeepInfra,
            messages = messages,
            stream = True
        )

        text = ""
        for chunk in res:
            text += chunk
            sys.stdout.write(f"\r{Color.BRIGHT_CYAN}[SkunaGPT]{Color.RESET} | {text}{Color.RESET}")
            sys.stdout.flush()
        print("\n")