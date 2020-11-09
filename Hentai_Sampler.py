# This is a simple program that uses the NHentai API to get random doujins
# dev: Zero Meia#8828

# this took too long pls end my misery

# Imports
from NHentai import NHentai
from os import system, name
from time import sleep
from colorama import init
from termcolor import colored
from random import randrange

# initializing colorama for colors
init()

# Variables
nhentai = NHentai()

# color variable used to randomize the color of the banner (cool)
colors = [
	'red',
	'green',
	'yellow',
	'magenta',
	'blue',
	'white']

# Functions
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

#Main function
def start(args):
	clear()
	print(colored('Last Link: {}\n', 'magenta').format(args))
	print(colored("""
██╗  ██╗███████╗███╗  ██╗████████╗ █████╗ ██╗
██║  ██║██╔════╝████╗ ██║╚══██╔══╝██╔══██╗██║
███████║█████╗  ██╔██╗██║   ██║   ███████║██║
██╔══██║██╔══╝  ██║╚████║   ██║   ██╔══██║██║
██║  ██║███████╗██║ ╚███║   ██║   ██║  ██║██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝╚═╝ Sampler\n""", colors[randrange(0, 6)]))
	print(colored('1 - Search With Tags', 'grey'))
	print(colored('2 - Random Dounjin\n', 'grey'))
	ch = input(colored('Input The Number Of Your Choice: ', 'cyan'))

	# if the choice is 1, run this mess
	if ch == '1':
		clear()
		print(colored("""
██╗  ██╗███████╗███╗  ██╗████████╗ █████╗ ██╗
██║  ██║██╔════╝████╗ ██║╚══██╔══╝██╔══██╗██║
███████║█████╗  ██╔██╗██║   ██║   ███████║██║
██╔══██║██╔══╝  ██║╚████║   ██║   ██╔══██║██║
██║  ██║███████╗██║ ╚███║   ██║   ██║  ██║██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝╚═╝ Searching With Tags\n""", colors[randrange(0, 6)]))
		ch = input(colored('Input Your Search Query: ', 'white'))
		search_obj: dict = nhentai.search(query=ch, sort='popular', page=1)
		slenght = len(search_obj['doujins'])
		with open('results.txt', 'w', encoding='utf-8') as f:
			i = 0
			if slenght == 0:
				print(colored('\nNo Results...', 'red'))
				print(colored('1 - Return to Start', 'grey'))
				print(colored('2 - Quit HentaiPicker', 'grey'))
				ch = input(colored('?: ', 'yellow'))
				if ch == '1':
					start('None')
				elif ch == '2':
					quit()
				else:
					print(colored('Unexpected Error, Returning...', 'red'))
					sleep(1.5)
					start('None')
			while i < slenght:
				search_results = search_obj['doujins'][i]['id']
				search_results = ' https://nhentai.net/g/'+search_results+'\n\n'
				f.write(search_results)
				i += 1
		print(colored('\nSearch Results Saved to results.txt\n', 'green'))
		print(colored('1 - Return to Start', 'grey'))
		print(colored('2 - Quit HentaiPicker', 'grey'))
		ch = input(colored('?: ', 'yellow'))
		if ch == '1':
			start('None')
		elif ch == '2':
			quit()
		else:
			print(colored('Unexpected Error, Returning...', 'red'))
			sleep(1.5)
			start('None')

	# if the choice is 2, run this other mess
	elif ch == '2':
		random_doujin: dict = nhentai.get_random()
		title = random_doujin['title']
		id = random_doujin['id']
		tags = str(random_doujin['tags'])
		link = 'https://nhentai.net/g/'+id
		artists = str(random_doujin['artists'])
		pages = str(random_doujin['pages'])
		remove = ["'", "]", "["]
		clear()
		print('\n')
		print(colored("""
██╗  ██╗███████╗███╗  ██╗████████╗ █████╗ ██╗
██║  ██║██╔════╝████╗ ██║╚══██╔══╝██╔══██╗██║
███████║█████╗  ██╔██╗██║   ██║   ███████║██║
██╔══██║██╔══╝  ██║╚████║   ██║   ██╔══██║██║
██║  ██║███████╗██║ ╚███║   ██║   ██║  ██║██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝╚═╝ Random\n""", colors[randrange(0, 6)]))
		print(colored('Title: {}\n', 'grey').format(title))
		for value in remove:
			tags = tags.replace(value, '')
		print(colored('Tags: {}\n', 'grey').format(tags))
		print(colored('Link: {}\n', 'magenta').format(link))
		for value in remove:
			artists = artists.replace(value, '')
		print(colored('Artist: {}\n', 'grey').format(artists))
		for value in remove:
			pages = pages.replace(value, '')
		print(colored('Pages: {}\n', 'grey').format(pages))
		print(colored('Returning to the start page in 5 seconds!', 'grey'))
		sleep(5)
		start(link)
	#if the choice isn't equal to 1 or 2 the program will treat the input as an error and will return to the start
	else:
		print(colored('Unexpected Error, Returning...', 'red'))
		sleep(1)
		start('None')
start('None')