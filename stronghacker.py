import platform
import lib
import os
import sys
from colorama import Fore, init
init(autoreset=True)

if platform.system() == 'Windows':
    os.system("cls")
elif platform.system() == "Linux":
    os.system("clear")

#question1 = input("\nThis tool was developed for educational purposes only\nDon't use it to make bad things.\n\nRemember. With great powers, comes great responsibility.\n- Stan Lee\n\nPress enter to continue...")

if platform.system() == 'Windows':
    os.system("cls")
elif platform.system() == "Linux":
    os.system("clear")

banner = f'''{Fore.RED}
 @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@  @@@   @@@@@@@@   @@@  @@@   @@@@@@    @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@
@@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@
!@@         @@!    @@!  @@@  @@!  @@@  @@!@!@@@  !@@         @@!  @@@  @@!  @@@  !@@       @@!  !@@  @@!       @@!  @@@
!@!         !@!    !@!  @!@  !@!  @!@  !@!!@!@!  !@!         !@!  @!@  !@!  @!@  !@!       !@!  @!!  !@!       !@!  @!@
!!@@!!      @!!    @!@!!@!   @!@  !@!  @!@ !!@!  !@! @!@!@   @!@!@!@!  @!@!@!@!  !@!       @!@@!@!   @!!!:!    @!@!!@!
 !!@!!!     !!!    !!@!@!    !@!  !!!  !@!  !!!  !!! !!@!! @ !!!@!!!!  !!!@!!!!  !!!       !!@!!!    !!!!!:    !!@!@!
     !:!    !!:    !!: :!!   !!:  !!!  !!:  !!!  :!!   !!:   !!:  !!!  !!:  !!!  :!!       !!: :!!   !!:       !!: :!!
    !:!     :!:    :!:  !:!  :!:  !:!  :!:  !:!  :!:   !::   :!:  !:!  :!:  !:!  :!:       :!:  !:!  :!:       :!:  !:!
:::: ::      ::    ::   :::  ::::: ::   ::   ::   ::: ::::   ::   :::  ::   :::   ::: :::   ::  :::   :: ::::  ::   :::
:: : :       :      :   : :   : :  :   ::    :    :: :: :     :   : :   :   : :   :: :: :   :   :::  : :: ::    :   : :


                                                                                                    Created By Bearlim
'''

def q():
    a = input("\nThis tool was developed for educational purposes only\nDon't use it to make bad things.\n\nRemember. With great powers, comes great responsibility.\n- Stan Lee\n\nPress enter to continue...")

def home():
    try:

        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system("clear")

        print(banner)

        print('''
[1] - Pentesting Tools
[2] - Social Engineering
[3] - Reverse Engineering
[4] - Exploitation Tools
[5] - Forensic Tools
[6] - Stress Tools
[7] - OSINT Tools
[8] - Wireless Tools
[0] - Exit

    ''')

        answer = input("Type an option:  ")
        answers = [str(x) for x in range(9)]

        while answer not in answers:
            print(f"{Fore.RED}Type a valid option!! ")
            answer = input()
        
        if answer == '1':
            return lib.pentesting()
        elif answer == '2':
            return lib.social()
        elif answer == '3':
            return lib.reverse()
        elif answer == '4':
            return lib.exploit()
        elif answer == '5':
            return lib.forensic()
        elif answer == '6':
            return lib.stress()
        elif answer == '7':
            return lib.osint()
        elif answer == '8':
            return lib.wireless()
        elif answer == '0':
            sys.exit("Good bye, i miss you (Y_Y) (´ᗣ｀) ")
    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C, Strong Hacker ლ(ಠ益ಠ)ლ")

if __name__ == '__main__':
    q()
    home()