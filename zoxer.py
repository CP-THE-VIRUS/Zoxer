import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

BY: CP THE VIRUS
IG : jblfxe

ZOXER HACKING TOOL 
""")

def display_menu():
    print(Fore.YELLOW + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    1. Ip-Scanner                   | 7. Sub-Domain-Scanner      
    2. Discord-Nuke                 | 8. DDOS-TOOL
    3. Subdirectory-Scanner         | 9. Discord-Token-Grabber
    4. Email-Boomber                | 10. Keylogger 
    5. Phone-Locator                | 11. Web-Crawler
    6. Port-Scanner                 | 12. Reverse-Shell 
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python ip-lookup.py"' if os.name == 'nt' else 'python ip-lookup.py')
    elif command == '2':
        os.system('cmd /k "python nuke-bot/main.py"' if os.name == 'nt' else 'python nuke-bot/main.py')
    elif command == '3':
        os.system('cmd /k "python Subdirectory-scanner/main.py"' if os.name == 'nt' else 'python Subdirectory-scanner/main.py')
    elif command == '4':
        os.system('cmd /k "python email-bomber.py"' if os.name == 'nt' else 'python email-bomber.py')
    elif command == '5':
        os.system('cmd /k "python phone-locator.py"' if os.name == 'nt' else 'python phone-locator.py')
    elif command == '6':
        os.system('cmd /k "python port-scanner.py"' if os.name == 'nt' else 'python port-scanner.py"')
    elif command == '7':
        os.system('cmd /k "python subdomain/main.py"' if os.name == 'nt' else 'python subdomain/main.py')
    elif command == '8':
        os.system('cmd /k "python ddos.py"' if os.name == 'nt' else 'python ddos.py')
    elif command == '9':
        os.system('cmd /k "python discord-token-grabber.py"' if os.name == 'nt' else 'python discord-token-grabber.py')
    elif command == '10':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Keylogger.py"')
    elif command == '11':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Web-Crawler.py"')
    elif command == '12':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Reverse-Shell.py"')
    else:
        print(Fore.RED + 'Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)