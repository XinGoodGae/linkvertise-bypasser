import requests
from os import name,system
from colorama import init, Fore
from datetime import datetime

init()
def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n")
def title():
	if name == 'posix':
	    stdout.write(f"\x1b]2;[ LinkVertise Bypasser By Github.com/XinGodDev ]\x07")
	elif name in ('ce', 'nt', 'dos'):
	    system(f'title [ LinkVertise Bypasser By Github.com/XinGodDev ]')
	else:
	    stdout.write(f"\x1b]2;[ LinkVertise Bypasser By Github.com/XinGodDev ]\x07")
def banner():
	print(f"""                                                 {Fore.LIGHTRED_EX}$$$$$$$$$$$$${Fore.RESET}        
                                            {Fore.LIGHTRED_EX}$$$$$$$$$$$$$$$$$$$$${Fore.RESET}    
                                          {Fore.LIGHTRED_EX}$$$$$$$$$$$$$$$$$$$$$$$$${Fore.RESET}  
                                         {Fore.LIGHTRED_EX}$$$$$$$$$$$$$$$$$$$$$$$$$$${Fore.RESET} 
                                        {Fore.LIGHTRED_EX}$$$$$$$$$$$$$$$$$$$$$$$$$$$$${Fore.RESET}
                                        {Fore.LIGHTRED_EX}$$$$$$$$${Fore.RESET}           {Fore.LIGHTRED_EX}$$$$$$$$${Fore.RESET}
                                        {Fore.LIGHTRED_EX}$$$$$${Fore.RESET}    111111111    {Fore.LIGHTRED_EX}$$$$$${Fore.RESET}
                                        {Fore.LIGHTRED_EX}$$$${Fore.RESET}    1111111111111    {Fore.LIGHTRED_EX}$$${Fore.RESET}
                                         {Fore.LIGHTRED_EX}$${Fore.RESET}  1111111111111111111  {Fore.LIGHTRED_EX}$${Fore.RESET} 
                                          {Fore.LIGHTRED_EX}${Fore.RESET} 111111111111111111111 {Fore.LIGHTRED_EX}${Fore.RESET}  
                                             1111111111111111111     
                                               1111111111111111      
                                                  1111111111         
                                                     1111            
                                                     1111            
                                                     1111  """)
clear()
title()
banner()
now = datetime.now()
time = now.strftime("%H:%M:%S")
linkvertise_url = str(input(f"\n{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.MAGENTA}Url to Bypass : {Fore.RESET}"))
r = requests.get(f"https://adlink-bypass-api-2.bigbypassalt.repl.co/api?={linkvertise_url}")
if r.status_code == 200:
	semi_bypassedlink = r.json()['bypassedlink']
	pass
else:
	print(r)
	print(r.text)
	exit()

rq = requests.get(semi_bypassedlink)
bypassed_link = rq.json()['data']["target"]
now = datetime.now()
time = now.strftime("%H:%M:%S")
print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Bypassed With Succes Result Url : {bypassed_link}")