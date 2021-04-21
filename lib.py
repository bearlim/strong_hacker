import returnn
import platform
import webbrowser
import sys
import os
from colorama import Fore, init
init(autoreset=True)

def pentesting():

    try:
        print('''
[1] - Nmap
[2] - Dnmap
[3] - DNSMap
[4] - Firewalk
[5] - Fragrouter
[6] - Ghost Phisher
[7] - Nikto
[8] - sslstrip
[9] - UnicornScan
[10] - Wireshark
[11] - twofi
[0] - Homescreen
        ''')

        answer = input("Type an option: ")
        answers = [str(x) for x in range(12)]

        while answer not in answers:
            print(f"{Fore.RED}Type a valid option")
            answer = input()
        
        if answer == '1': # Nmap
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://nmap.org/download.html")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("sudo apt install nmap -y"))
                print("If everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '2': # Dnmap
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/Seabreg/dnmap")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/Seabreg/dnmap.git tools/dnmap"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '3': #DNSMap
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/dnsmap")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/dnsmap.git tools/dnsmap"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '4': # Firewalk
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/firewalk")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/firewalk.git tools/Firewalk"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '5': # Fragrouter
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/fragrouter")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/fragrouter.git tools/Fragrouter"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '6': # Ghost Phisher
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/ghost-phisher")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/ghost-phisher.git tools/ghost_phisher"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '7': # Nikto
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/nikto")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/nikto.git tools/nikto"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '8': # sslstrip
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/sslstrip")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/sslstrip.git tools/sslstrip"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '9': # UnicornScan
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/unicornscan")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/unicornscan.git tools/unicornscan"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '10': # Wireshark
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/wireshark")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/wireshark.git tools/wireshark"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '11': # twofi
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/twofi")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/twofi.git tools/twofi"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        elif answer == '0': # Homescreen
            return returnn.home()
    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C, Strong Hacker (ノಠ益ಠ)ノ彡┻━┻ ")
    
def social():
    try: 
        print(''''
[1] - SocialFish
[2] - Set (SetToolkit)
[3] - PHEmail
[4] - Facebrok
[5] - Catphish
[0] - Homescreen
        ''')
        answer = input("Type an option:  ")
        answers = [str(x) for x in range(6)]

        while answer not in answers:
            print(f"{Fore.RED}Type a valid option!!")
            answer = input()
        
        if answer == '1':
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/UndeadSec/SocialFish")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/UndeadSec/SocialFish.git tools/socialfish"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '2': # Set
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/trustedsec/social-engineer-toolkit")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git tools/set"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '3': # PHEmail
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/Dionach/PhEmail")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/Dionach/PhEmail.git tools/PHEmail"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '4': # Facebrok
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/PowerScript/facebrok")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/PowerScript/facebrok.git tools/facebrok"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '5': # Catphish
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/ring0lab/catphish.git")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/ring0lab/catphish.git tools/catphish"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '0':
            return returnn.home()
        
    except KeyboardInterrupt:
        sys.exit("U pressed CTRL + C, strong hacker (ノಠ益ಠ)ノ彡┻━┻ ")
def reverse():
    try:
        print(''''
[1] - ApkTool
[2] - ApkStudio
[3] - Scanmen
[4] - edb-debugger
[5] - dex2jar
[0] - Homescreen
        ''')
        answer = input("Type an option: ")
        answers = [str(x) for x in range(6)]
        while answer not in answers:
            print(f"{Fore.RED}Type a valid option!!")
            answer = input()
        
        if answer == '0':
            return returnn.home()

        elif answer == '1': # ApkTool
            answer1 = input("Do you want go to website? [Y/n]")
            while answer1.lower() not in ['y', 'n', '']:
                print(f'{Fore.RED}Type a valid option: ')
                answer1 = input()
            
            if answer1.lower() == 'y':
                webbrowser.open("https://ibotpeaches.github.io/Apktool/")
            elif bool(answer1) == False:
                webbrowser.open("https://ibotpeaches.github.io/Apktool/")
            elif answer1.lower() == 'n':
                print("This is the website: https://ibotpeaches.github.io/Apktool/")


            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


        elif answer == '2': # ApkStudio
            answer1 = input("Do you want go to website? [Y/n]")
            while answer1.lower() not in ['y', 'n', '']:
                print(f'{Fore.RED}Type a valid option: ')
                answer1 = input()
            
            if answer1.lower() == 'y':
                webbrowser.open("https://vaibhavpandey.com/apkstudio/")
            elif bool(answer1) == False:
                webbrowser.open("https://vaibhavpandey.com/apkstudio/")
            elif answer1.lower() == 'n':
                print("This is the website: https://vaibhavpandey.com/apkstudio/")


            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '3': # Scanmen
            
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/scanmem/scanmem")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/scanmem/scanmem.git tools/scanmem"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '4': # edb-debugger
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/edb-debugger")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/edb-debugger.git tools/edb-debugger"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


        elif answer == '5': # dex2jar
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/dex2jar")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/dex2jar.git tools/dex2jar"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻ ")

def exploit():
    try:
        print('''
[1] - Armitage
[2] - Backdoor factory
[3] - BeFF
[4] - ShellNoob
[5] - sqlmap
[6] - Routersploit 
[7] - Metasploit Framework
[0] - Homescreen
        ''')
        answer = input("Type an option:  ")
        answers = [str(x) for x in range(8)]

        while answer not in answers:
            print(f"{Fore.RED}Type a valid option: ")
            answer = input()
            
        if answer == '1': # Armitage
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/armitage")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/armitage.git tools/armitage"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '0': # Home
            return returnn.home()

        elif answer == '2': # Backdoor factory
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/backdoor-factory")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/backdoor-factory.git tools/backdoor-factory"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '3': # BeFF
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/beef-xss")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/beef-xss tools/beef_xss"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '4': # ShellNoob
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/shellnoob")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/shellnoob.git tools/shellnoob"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '5': # sqlmap
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://gitlab.com/kalilinux/packages/sqlmap")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/sqlmap.git tools/sqlmap"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '6': # Routersploit
            if platform.system() == 'Windows':
                print(f"Your platform is {platform.system()}, so, you have to install\nLink: https://github.com/threat9/routersploit")
                
                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/threat9/routersploit.git tools/routersploit"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

                # Go to homescreen
                answer = input("Back to homescreen? [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("Type a valid option:")
                    answer = input()
                if answer.lower() == 'y':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'n':
                    sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '7': # Metasploit
            if platform.system() == "Windows":
                answer1 = input("Do you want go to Metasploit's github? [Y/n]")
                while answer1 not in ['y', 'n', '']:
                    print(f"{Fore.RED}Type a valid option: ")
                    answer1 = input()
                
                if answer1.lower() == 'y':
                    webbrowser.open("https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers")
                elif bool(answer1) == False:
                    webbrowser.open("https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers")
                elif answer1.lower() == 'n':
                    print("You can go to web site: https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers")
            elif platform.system() == "Linux":
                answer1 = input("Do you want to install now the metasploit? [y/n]")
                
                while answer1 not in ['y', 'n', '']:
                    print(f"{Fore.RED}Type a valid option: ")
                    answer1 = input()
                if answer1.lower() == 'y':
                    print(os.system("cd ~ && mkdir metasploit && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall &&  chmod 755 msfinstall && ./msfinstall"))
                elif bool(answer1) == False:
                    print(os.system("cd ~ && mkdir metasploit && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall &&  chmod 755 msfinstall && ./msfinstall"))
                elif answer1.lower() == 'n':
                    print("Go to the website and install the metasploit: https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers")

            
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻ ")

def forensic():
    try:
        print("""

[1] - Binwalk
[2] - iPhone backup analyzer
[3] - Dumpzilla
[4] - Cuckoo
[5] - DiStorm3
[0] - Homescreen
        """)
        answer = input("Type an option: ")
        answers = [str(x) for x in range(6)]
        
        while answer not in answers:
            print(f"{Fore.RED}Type a valid option!!")
            answer = input()
        if answer == '0': # Home
            return returnn.home()

        elif answer == '1':  # Binwalk
            if platform.system() == 'Windows':
                print("Go to website and download it: https://gitlab.com/kalilinux/packages/binwalk")
            elif platform.system() == "Linux":
                print(os.system("git clone https://gitlab.com/kalilinux/packages/binwalk.git tools/binwalk"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '2':  # iPhone
            if platform.system() == 'Windows':
                print("Go to website and download it: https://gitlab.com/kalilinux/packages/iphone-backup-analyzer")
            elif platform.system() == "Linux":
                print(os.system("git clone https://gitlab.com/kalilinux/packages/iphone-backup-analyzer.git tools/iphone_backup_analyzer"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '3':  # Dumpzilla
            if platform.system() == 'Windows':
                print("Go to website and download it: https://gitlab.com/kalilinux/packages/dumpzilla")
            elif platform.system() == "Linux":
                print(os.system("git clone https://gitlab.com/kalilinux/packages/dumpzilla.git tools/dumpzilla"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '4':  # Cuckoo 
            if platform.system() == 'Windows':
                print("Go to website and download it: https://gitlab.com/kalilinux/packages/cuckoo")
            elif platform.system() == "Linux":
                print(os.system("git clone https://gitlab.com/kalilinux/packages/cuckoo.git tools/cuckoo"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '5':  # DiStorm3
            if platform.system() == 'Windows':
                print("Go to website and download it: https://gitlab.com/kalilinux/packages/distorm3")
            elif platform.system() == "Linux":
                print(os.system("git clone https://gitlab.com/kalilinux/packages/distorm3.git tools/distorm3"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")

            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻ ")

def stress():
    try:
        print('''
[1] - t50
[2] - mdk3
[3] - Impulse
[0] - Homescreen
        ''')
        answer = input("Type an option:  ")
        answers = [str(x) for x in range(4)]

        while answer not in answers:
            print(f"{Fore.RED}Type a valid option")
            answer = input()
        
        if answer == '0':
            return returnn.home()
        
        elif answer == '1':  # t50 
            if platform.system() == 'Windows':
                print("go to website and download the tool: https://gitlab.com/fredericopissarra/t50")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/fredericopissarra/t50.git tools/t50"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
            
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


        elif answer == '2':  # mkd3
            if platform.system() == 'Windows':
                print("go to website and download the tool: https://gitlab.com/kalilinux/packages/mdk3")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/mdk3.git tools/mdk3"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
            
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '3':  # DHCPig
            if platform.system() == 'Windows':
                print("go to website and download the tool: https://github.com/LimerBoy/Impulse")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/LimerBoy/Impulse.git tools/impulse"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
            
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻")

def osint():
    try:
        print('''
[1] - Fluxion
[2] - Sherlock
[3] - osi.ig
[4] - Instagramosint
[5] - Email2Phonenumber
[0] - Homescreen
        ''')
        answer = input("Type an option:  ")
        answers = [str(x) for x in range(6)]
        
        while answer not in answers:
            print(f"{Fore.RED}Type a valid option!!")
            answer = input()

        if answer == '0':
            return returnn.home()

        elif answer == '1':  # Fluxion
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/FluxionNetwork/fluxion")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/FluxionNetwork/fluxion.git tools/fluxion"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


        elif answer == '2':  # Sherlock
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/sherlock-project/sherlock")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/sherlock-project/sherlock.git tools/sherlock"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
     

        elif answer == '3':  # osi.ig
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/th3unkn0n/osi.ig")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/th3unkn0n/osi.ig.git tools/osi_ig"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")
        
        elif answer == '4':  # Instagramosint
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/sc1341/InstagramOSINT")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/sc1341/InstagramOSINT.git tools/instragram_osint"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

        elif answer == '5':  # Email2Phonenumber
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/martinvigo/email2phonenumber")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/martinvigo/email2phonenumber.git tools/email2phonenumber"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")

    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻ ")

def wireless():
    try:
        print('''
[1] - Aircrack package
[2] - WifiPhisher
[3] - Fuzzap
[4] - Bully
[0] - Homescreen
        ''')
        answer = input("Type an option: ") 
        answers = [str(x) for x in range(6)]
        
        while answer not in answers:
            print(f"{Fore.RED}Type a valid option: ")
            answer = input()
        if answer == '0':
            return returnn.home()

        elif answer == '1':
            answer1 = input("Do you want go to website? [Y/n]")
            while answer1.lower() not in ['y', 'n', '']:
                print(f'{Fore.RED}Type a valid option: ')
                answer1 = input()
            
            if answer1.lower() == 'y':
                webbrowser.open("https://www.aircrack-ng.org/")
            elif bool(answer1) == False:
                webbrowser.open("https://www.aircrack-ng.org/")
            elif answer1.lower() == 'n':
                return returnn.home()
            
            
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


        elif answer == '2':
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/wifiphisher/wifiphisher")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/wifiphisher/wifiphisher.git tools/wifiphisher"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


        elif answer == '3':
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/PlantDaddy/FuzzAP")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/PlantDaddy/FuzzAP.git tools/fuzzap"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")



        elif answer == '4':
            if platform.system() == 'Windows':
                print("Go to website and download the tool: https://github.com/aanarchyy/bully")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/aanarchyy/bully.git tools/bully"))
                print("The tool are in \"tools\" path\nIf everything gonna be okay, now you are a strong hacker ᕦ(ò_óˇ)ᕤ")
        
            # Go to homescreen
            answer = input("Back to homescreen? [Y/n]  ")
            while answer.lower() not in ['y', 'n', '']:
                print("Type a valid option:")
                answer = input()
            if answer.lower() == 'y':
                return returnn.home()
            elif bool(answer) == False:
                return returnn.home()
            elif answer.lower() == 'n':
                sys.exit("Good bye, strong hacker ᕦ(ò_óˇ)ᕤ")


    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻ ")