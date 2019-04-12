from pyfiglet import figlet_format
from termcolor import colored


def print_ascii_msg(words,color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
	if color not in valid_colors:
		color = "red"  #default color
	ascii_msg = figlet_format(words)
	colored_art = colored(ascii_msg, color=color, attrs = ["blink"])
	print(colored_art)

words = input("What words would you like to print? ")
color = input("What color would you like this in? ")
print_ascii_msg(words,color)