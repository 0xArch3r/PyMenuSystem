import getpass, os, subprocess, socket
from datetime import datetime

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class BaseMenu:
    def __init__(self, title):
        self._title = title
        self._menu = {}

    def _chooser(self):
        choice = ""
        while choice not in self._menu.keys() or "blank" in choice:
            choice = input("Please select: ")
            if choice == "r" or choice == "R":
                return 0
            if choice == "rr" or choice == "RR":
                return 99
        x = self._menu[choice]['function'].run()
        return x
    
    def _header(self):
        curr_date = datetime.now()
        user = getpass.getuser()
        last_str = subprocess.getoutput(f"last {user} | head -1 | cut -c40-55")
        hostname = socket.gethostname()

        print(f"Welcome {color.RED}{user}{color.END} last login to {color.PURPLE}{hostname}{color.END} at {color.BLUE}{last_str}{color.END}")
        print(f"Current System Time: {curr_date}")
        print("\n------------------------------------------------------")
        print(f"===== {color.RED}DEVELOPMENT Menu System{color.END} =====\n")

    def _footer(self):
        ip_address = socket.gethostbyname(socket.gethostname())
        print("\n------------------------------------------------------\n")
        print(f"Menu Version:\t\t1.0.0")
        print(f"IP Address:\t\t{ip_address}")
        print("")

    def append_to_menu(self, option=None, title=None, function=None):
        self._menu[str(option)] = {"title": title, "function":function}


    def run_menu(self):
        x = -1
        while True:
            os.system("clear")
            self._header()
            print(f"\t\t>>> {self._title} <<<\n")

            for option, values in self._menu.items():
                if values['title'] != None :
                    print(f"\t{option}: {values['title']}") 
                else:
                    print("")

            self._footer()
            x = self._chooser()
            if x == 0:
                return 0
            if x == 99:
                return 99