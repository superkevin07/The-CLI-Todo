from time import sleep
from colorama import Fore, Style, init
init(autoreset = True)


print(f"{Fore.CYAN}{Style.BRIGHT}[CONSOLE] initializing...")
sleep(3)
file = open("todo.md", "w+")
print(f"{Fore.CYAN}{Style.BRIGHT}[CONSOLE] there we go...")
sleep(1.5)
print(f"\n\n{Fore.CYAN}{Style.BRIGHT}[CONSOLE] Todo")

def check():
	uin = input("[USER] ")

	if uin != "done@":
		file.write("\n- [] " + uin)
		check()
	else:
		print(f"\n{Fore.CYAN}{Style.BRIGHT}[CONSOLE] finished, now you can open the markdown file genertated and uncheck all of the boxes and cut paste the file in your desired location.\nNOTE : The file is named as 'todo.md'.")
		print(f"\n{Fore.CYAN}{Style.BRIGHT}[CONSOLE] Press 'Enter' to quit...")
		input()

check()
