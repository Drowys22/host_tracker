import time
from fileinput import close
from os import close

from ping3 import ping
from colorama import Fore, Style, init
import socket
import requests

maxnum = 1

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BLACK = "\033[90m"
RESET = "\033[0m"

ownhostname = socket.gethostname()
ownlocal_ip = socket.gethostbyname(ownhostname)
public_ip = requests.get("https://api.ipify.org").text


print(RED + "[" + RESET + "system" + RED + "]")
print(RED + "[" + RESET + "system" + RED + "]")
print(RED + "[" + RESET + "system" + RED + "]")
print(RED + "[" + RESET + "system" + RED + "]" + RESET +" Your Datas:")
print(RED + "[" + RESET + "system" + RED + "]" + RESET +" Local IP:" + RED + ownlocal_ip)
print(RED + "[" + RESET + "system" + RED + "]" + RESET +" Public IP:" + RED + public_ip)
print(RED + "[" + RESET + "system" + RED + "]")
print(RED + "[" + RESET + "system" + RED + "]")
print(RED + "[" + RESET + "system" + RED + "]")
HOST = input(RED + "[" + RESET + "Enter The " + YELLOW + "Target" + RED + "]   " + RESET)


try:
    host_ip = socket.gethostbyname(HOST)
except socket.gaierror:
    host_ip = "Unknown IP"



print(RED + "[" + MAGENTA + "TRACKING" + RED + "]" + RESET)
print(RED + "[" + MAGENTA + "Ctrl+c to exit!" + RED + "]" + RESET)
time.sleep(2.5)
print(RED + "[" + CYAN + "Fast" + RESET + " mode" + RED + "]" + RESET)
print(RED + "[" + GREEN + "Tracked!" + RED + "]" + RESET)
time.sleep(3)

while True:
    result = ping(HOST, unit="ms")



    if result is None or result == 0:
        print(RED + "["+ RESET + "System" + RED + "][" + RESET + f"{HOST}" + RED + "] " + MAGENTA + "Host unreachable / " + RED +"ERROR" + RESET)
    else:
        ping_time = round(result, 1)
        if ping_time < 50:
            color = Fore.GREEN
        elif ping_time < 100:
            color = Fore.YELLOW
        elif ping_time < 1:
            print(RED + "[" + RESET + "System" + RED + "][" + RESET + f"{HOST}" + RED +"]" + MAGENTA + f"Host is down! - "+ RED + "ERROR" + RESET)
        else:
            color = Fore.RED


        print(RED + "[" + RESET + f"{maxnum}" + RED + "][" + RESET + f"{HOST}" + RED +"]" + MAGENTA + "Ping:" + MAGENTA + f"{ping_time} ms" + BLACK + "  []  " + MAGENTA + "IP:"+ MAGENTA + f"{host_ip}" + BLACK + "  []  " +RESET)

    maxnum += 1

